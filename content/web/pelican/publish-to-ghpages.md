title: Automatic page publication from Pelican to GitHub Pages
tags: pelican, gh-pages, gh-actions

I want to automatically generate and publish the website when I push a modification to the master branch
of the GitHub repository.


The `tasks.py` script already includes a task to help publishing to gh-pages.
To use it, we need to install `invoke`. The `gp-pages` task also need the
[`ghp-import`](https://github.com/c-w/ghp-import) package.
Finally, while we do not need it for the publication task, the `livereload` package
is useful for development, to allow calling `invoke livereload`.

Here is my `requirements.txt` file, will all those dependencies, and a few others I use for my site:

    :::txt
    ghp-import
    invoke
    livereload
    markdown
    pelican
    typogrify


On GitHub, the `master` branch contains the sources of the site, and the `gh-pages` branch
contains the published website. There are other ways to do it, for instance by publishing
a subdirectory as the website, but I prefer to work with different branches. 
The `ghp-import` package makes it easy to manage the `gh-pages` branch.


I tweaked a little bit the `tasks.py` file. First, I set the name of the branch where to publish:

    :::python
        'github_pages_branch': 'gh-pages',

I also changed some options passed to the `ghp-import` script:

    :::python
    @task
    def gh_pages(c):
        """Publish to GitHub Pages"""
        preview(c)
        c.run('ghp-import -n -b {github_pages_branch} '
              '-m {commit_message} '
              '{deploy_path}'.format(**CONFIG))

I added the `-n` option to create the `.nojekyll` file. This tells GitHub to not invoke Jekyll
on the generated contents. I removed the `-p` option, as I need to include credentials to publish
the pages.


Finally, here is the GitHub Actions configurations:

    :::yaml
    name: Publish Website
    on:
    push:
      branches: [ master ]
    jobs:
    publish:
      runs-on: ubuntu-latest
      steps:
      - uses: actions/checkout@v2
        with:
          submodules: true
      - name: Set up Python
        uses: actions/setup-python@v1
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Build docs
        run: invoke gh-pages
      - name: Publish docs
        run: git push -f "https://${GITHUB_ACTOR}:${{secrets.TOKEN}}@github.com/${GITHUB_REPOSITORY}.git" gh-pages:gh-pages

The action run when I push to `master` branch.

The checkout action tells to checkout submodules as well, as I use submodules for the Flex theme, and for pelican-plugins.

I install Python packages from the requirements.txt file.

I call the invoke task to create the (local) gh-pages branch with the published contents.

Finally, I force push the gh-pages branch to GitHub, using the required credentials.
