# Pygame Template

[![Coverage][coverage-image]][coverage-url]
[![Codacy][codacy-image]][codacy-url]

[![Appveyor Build Status][appveyor-image]][appveyor-url]

[![Travis CI Build Status][travis-ci-image]][travis-ci-url]

[![Circle CI Build Status][circle-ci-image]][circle-ci-url]

[![Codeship Build Status][codeship-image]][codeship-url]

This is my pygame template. It allows for a smooth reactive typing interface,
as all keyboard inputs are well defined.
Mouse inputs and other standard things like screen size are already defined too.


[appveyor-image]: https://ci.appveyor.com/api/projects/status/ex4iedu3u9hdae2w/branch/master?svg=true
[appveyor-url]: https://ci.appveyor.com/project/AndyDeany/pygame-template
[travis-ci-image]: https://travis-ci.org/AndyDeany/pygame-template.svg?branch=v0.5.0
[travis-ci-url]: https://travis-ci.org/AndyDeany/pygame-template
[circle-ci-image]: https://circleci.com/gh/AndyDeany/pygame-template.svg?style=shield&circle-token=:circle-token
[circle-ci-url]: https://circleci.com/gh/AndyDeany/pygame-template
[codeship-image]: https://app.codeship.com/projects/486535b0-a44a-0134-b91e-463a26eaa663/status?branch=master
[codeship-url]: https://app.codeship.com/projects/190482
[coverage-image]: https://api.codacy.com/project/badge/Coverage/8767091123c14b6a90ec5902069b4c9e
[coverage-url]: https://www.codacy.com/app/AndyDeany/pygame-template?utm_source=github.com&utm_medium=referral&utm_content=AndyDeany/pygame-template&utm_campaign=Badge_Coverage
[codacy-image]: https://api.codacy.com/project/badge/Grade/8767091123c14b6a90ec5902069b4c9e
[codacy-url]: https://www.codacy.com/app/AndyDeany/pygame-template?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=AndyDeany/pygame-template&amp;utm_campaign=Badge_Grade

# Docs

## Environment variables

`pygametemplate` provides some environment variables that you can set to
change the functionality of some things at run time.
These are detailed below.

### `TEST`

When you are running automated tests against your game,
there are some things that you want to function slightly differently.

In order to enable automated testing mode,
you should set the `TEST` environment variable to `"1"`.
You can do this in Python like so:

```Python
import os


os.environ["TEST"] = "1"
```

This enables the following functionality:

* `core.log()` will reraise the last thrown exception,
instead of doing `raise CaughtFatalException`.
This makes it easier to test that your functions/methods raise
the errors you expect them to, as they will just raise these errors.

* `core.log()` will not open a popup window on fatal errors.
This is because interacting with this window from automated tests is very difficult.
