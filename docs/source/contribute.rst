.. _chap_contribute:

Contribute
===========

Researchers
-----------

Survey
^^^^^^

Please first fill out this VERY brief survey about the consent forms
for your studies: http://goo.gl/forms/2lsmYcOsAs . It only has a few
questions and should take a few minutes to fill out.  Even if
your consent form doesn't yet include any provision for data sharing,
your contribution would be very valuable (although it would consist of
simply saying "No").

Additional Materials
^^^^^^^^^^^^^^^^^^^^

To add to the materials on this site, please open an issue on our `GitHub issues`_ page or even send a new pull request via `GitHub pull requests`_. In particular, we're looking for:

- samples of consent forms allowing re-distribution/deposit to
  public archives 

- relevant publications and discussions

- changes/recommendations for the **ultimate** consent form formulation

For sample consent forms, see the instructions below for how to submit pull requests.  If submitting consent forms via `GitHub issues`_, please include a full URL to the consent form and the desired filename you'd like to see it represented as on the samples_ page.  Note that for the URL you submit, `persistent URLs`_ such as `DOIs`_ are ideal, since these will not require frequent updates to this site in the event that a link moves.

Adding Sample Consent Forms via git-annex
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Although you can add new sample consent forms by simply opening an issue on the `GitHub issues`_ page with a full URL and a desired filename, your request will be expedited if you file a pull request instead.  To do this, first install `git-annex`_ for your platform:

**Debian/Ubuntu**

.. code-block:: bash

   sudo apt-get install neurodebian
   sudo apt-get install git-annex-standalone

**CentOS/RHEL**

.. code-block:: bash

   sudo yum install epel-release
   sudo yum install git-annex

**Mac OS X**

For Mac OS X, you will first need to install `HomeBrew`_ using the instructions on their site.  You will also need to download the `Apple Xcode`_ command line tools.  This can be accomplished by running the following:

.. code-block:: bash

   xcode-select --install

After this is finished, run the following command to install `git-annex`_:

.. code-block:: bash

   brew install git-annex

After `git-annex`_ is installed, you'll need to `fork`_ the `GitHub repository`_ that this website is built from.  When you're done forking, clone down the repository and navigate to the ``samples`` directory.

.. code-block:: bash

   git clone https://github.com/[YOUR USERNAME GOES HERE]/open-brain-consent.git
   cd open-brain-consent/samples

Then, use `git-annex`_ to add a reference to the URL of your consent form.  The ``--file=`` flag allows you to specify a custom filename- without it, `git-annex`_ will generate a filename based off the URL.  When you're done, commit and push your changes to your fork:

.. code-block:: bash

   git annex addurl [YOUR URL HERE] --file=[YOUR DESIRED FILENAME HERE]
   git add [YOUR DESIRED FILENAME HERE]
   git commit -m "Added [YOUR DESIRED FILENAME HERE]"
   git push

This should update both the ``master`` and ``git-annex`` branches on your fork.  Submit two `GitHub pull requests`_- one for ``master`` and one for ``git-annex``.

Updating Sample Consent Forms via git-annex
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Occasionally, a URL for a consent form on the samples_ page breaks and needs to be updated.  To fix a broken link, install `git-annex`_, create a fork of the `GitHub repository`_, and clone it using the instructions above.  Navigate to ``samples`` and run the ``rmurl`` subcommand as follows:

.. code-block:: bash

   git annex rmurl [FILENAME] [BROKEN URL]
   git annex addurl [NEW URL] --file=[FILENAME]
   git push
 
This will only update the ``git-annex`` branch.  Submit a pull request for just this branch.

IRB committee members
---------------------

We would welcome your feedback very much, in particular:

- What concerns on public sharing of neuroimaging data you might have
  if all identifiable information is removed (e.g. skull stripped) and
  subjects agreed to those terms.

- What particular consent form composition and wording aspects would
  you recommend (e.g. "make it an explicit additional form requiring
  a separate signature") and why?

Contact information
===================

- Directly via email at open-brain-consent@datalad.org
- `GitHub issues`_ page

.. _GitHub issues: https://github.com/datalad/open-brain-consent/issues
.. _GitHub pull requests: https://github.com/datalad/open-brain-consent/pulls
.. _persistent URLs: https://en.wikipedia.org/wiki/Persistent_uniform_resource_locator
.. _DOIs: https://doi.org/10.1000/182
.. _HomeBrew: https://brew.sh/
.. _Apple Xcode: https://developer.apple.com/xcode/
.. _git-annex: https://git-annex.branchable.com/
.. _samples:
.. _GitHub repository: https://github.com/datalad/open-brain-consent
.. _fork: https://help.github.com/articles/fork-a-repo/
