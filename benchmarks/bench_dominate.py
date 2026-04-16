#!/usr/bin/env python3
"""Lightweight performance benchmarks for dominate.

Usage:
  python benchmarks/bench_dominate.py
  python benchmarks/bench_dominate.py --repeats 7 --iterations 100
"""

import argparse
import gc
import statistics
import time

from dominate import document, tags, util


def _make_text(i):
    return "text %d & <tag> \"quoted\"" % i


def build_tree(depth, breadth, with_attrs=False):
    node = tags.div()
    if with_attrs:
        node["class"] = "bench"
        node["data_id"] = "123"
        node["title"] = "bench title"
    if depth <= 0:
        node.add(_make_text(0))
        return node
    for i in range(breadth):
        child = build_tree(depth - 1, breadth, with_attrs=False)
        child.add(_make_text(i))
        node.add(child)
    return node


def bench_build_render_small():
    doc = document(title="Bench")
    doc.add(build_tree(depth=3, breadth=4, with_attrs=True))
    return doc.render()


def bench_render_large_existing(tree):
    return tree.render()


def bench_context_heavy():
    root = tags.div()
    with root:
        for i in range(40):
            with tags.section():
                tags.h1(_make_text(i))
                for j in range(6):
                    tags.p(_make_text(i * 10 + j))
    return root.render()


def bench_lazy_render():
    def lazy_value(i):
        return "lazy %d" % i

    root = tags.div()
    for i in range(200):
        root.add(util.lazy(lazy_value, i))
    return root.render()


def bench_table_add():
    table = tags.table()
    for _ in range(10000):
        row = tags.tr()
        for _ in range(20):
            row.add(tags.td("x"))
        table.add(row)
    return table.render()


def bench_table_with():
    table = tags.table()
    for _ in range(10000):
        row = tags.tr()
        with row:
            for _ in range(20):
                tags.td("x")
        table.add(row)
    return table.render()


def _run_benchmark(name, func, iterations, repeats, disable_gc):
    # Warm up
    func()

    if disable_gc:
        gc.disable()

    try:
        times = []
        for _ in range(repeats):
            start = time.perf_counter()
            for _ in range(iterations):
                func()
            end = time.perf_counter()
            times.append((end - start) / iterations)
    finally:
        if disable_gc:
            gc.enable()

    mean = statistics.mean(times)
    median = statistics.median(times)
    minimum = min(times)
    return {
        "name": name,
        "iterations": iterations,
        "mean": mean,
        "median": median,
        "min": minimum,
    }


def _format_ms(seconds):
    return "%.3f" % (seconds * 1000.0)


def main():
    parser = argparse.ArgumentParser(description="Dominate performance benchmarks")
    parser.add_argument("--repeats", type=int, default=5, help="Number of repeats")
    parser.add_argument(
        "--iterations",
        type=int,
        default=None,
        help="Override per-benchmark iteration counts",
    )
    parser.add_argument(
        "--no-gc",
        action="store_true",
        help="Disable GC during timed sections",
    )
    args = parser.parse_args()

    large_tree = build_tree(depth=5, breadth=4, with_attrs=True)

    benchmarks = [
        ("build+render_small", bench_build_render_small, 80),
        ("render_large_existing", lambda: bench_render_large_existing(large_tree), 200),
        ("context_heavy_build+render", bench_context_heavy, 60),
        ("lazy_render", bench_lazy_render, 80),
        ("table_add_10k_x_20", bench_table_add, 1),
        ("table_with_10k_x_20", bench_table_with, 1),
    ]

    results = []
    for name, func, iters in benchmarks:
        iterations = args.iterations if args.iterations is not None else iters
        results.append(_run_benchmark(name, func, iterations, args.repeats, args.no_gc))

    header = "{:<28} {:>10} {:>10} {:>10} {:>10}".format(
        "benchmark", "iters", "mean_ms", "p50_ms", "min_ms"
    )
    print(header)
    print("-" * len(header))
    for row in results:
        print(
            "{:<28} {:>10} {:>10} {:>10} {:>10}".format(
                row["name"],
                row["iterations"],
                _format_ms(row["mean"]),
                _format_ms(row["median"]),
                _format_ms(row["min"]),
            )
        )


if __name__ == "__main__":
    main()
