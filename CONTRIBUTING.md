
# 1. Welcome additions

Anything that is part of the official HTML spec is likely welcome.

Common patterns of web development, or ease-of-use features are welcome, so long as they are general and are likely to be useful to a broad group and not targetting any specific implimentation.

## 1.1. Testing

All PRs must have 100% test coverage of new code.

New features should include example usage, including motivations.



# 2. Not interested

For exceptions to these, see #Community

## 2.2. No 3rd party dependencies

Do not add 3rd party dependencies.

## 2.3. No 3rd party integrations

I am not interested in maintaining integrations with a bunch of random JS/web frameworks/libraries. (i.e. HTMX, Flask, Unpoly, whatever)


# 3. Community Packages

If you wish to add a feature that would otherwise be disallowed by the above, you can make a community package. See `community/htmx.py` for a trivial example.

Community packages must not be referenced from the main library, and must not do anything unless explicitly imported.

