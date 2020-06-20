.. _chap_gdpr:

GDPR edition
============

Context
-------
Responsible and ethical sharing of data and code that underlie the results of scientific work is an important step towards improving research transparency, fostering inclusivity and building public trust in science.
At the same time, privacy of sensitive personal data, including neuroimaging data, is highly important.
Ethical review boards at research institutions are responsible for reviewing a study protocol and deciding whether it can continue based on its adherence to the relevant ethical and research integrity principles, which typically include regulations on personal data privacy.
In the European Union, such data privacy requirements are subject to the `General Data Protection Regulation`_ (GDPR) as implemented by its member countries.
Despite the increased importance that funders and institutions are currently placing on open science practices, no clear, thorough and openly available guides exist for publicly sharing neuroimaging data under the GDPR.
Our goal is to share community-contributed templates for consent forms and other documentation required for ethical approval of brain research data processing and sharing under the GDPR.

History and links
~~~~~~~~~~~~~~~~~
Several people and groups have contributed to this project over the past years.
Below are some links pointing to events/initiatives where work was done on the templates.

- `Initial GitHub issue`_ suggesting that GDPR should be added to the Open Brain Consent templates
- `OHBM Hackathon 2019 project`_ aiming to create GDPR compatible templates and educational content
- `Work-in-progress Google document`_ attempting to distill the core concepts of the GDPR as they relate to brain imaging research data
- `GliMR COST workshop<https://glimr.eu/post/hackathon/>`_ to update templates to include clinical research and a data user agreement

The final push to make the GDPR version of the open brain consent took place during a GLiMR workshop (`COST
<https://www.cost.eu/>`_ action CA18206) the 27th Novembre 2019, COST Association, 149 Avenue Louise, Brussels.
See :ref:`GDPR/credit <chap_gdpr_credit>` document for more information.

More info:

.. toctree::
   :maxdepth: 1

   credit.rst


Summary of GDPR-related updates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Several forms are typically necessary when applying for approval from an ethical review board to conduct and share brain imaging research.
This includes (but is not limited to) the study protocol, a patient or participant information letter, a consent form, and extra information.
While the types and formats of these forms vary between countries and institutions, the GDPR requires attention to specific details that are mostly standard across EU member states.
In order to work these forms and GDPR additions into standardized templates, the following organizational structure is given.
It distinguishes between forms that would typically follow the format required by the institution, and forms for which the goal is to provide a standardized template:

.. image:: /_static/delineating_templates_gdpr.png

In short, the process starts with the institution-based ethics application that explains the study and its purpose, but would typically also include a patient/participant information letter and a consent form for the study of interest.
These forms then refer to GDPR-specific templates (provided here or separate documents).


.. _chap_gdpr_documents:

GDPR Documents
--------------

.. toctree::
   :maxdepth: 3

   ultimate_gdpr.rst
   data_privacy_impact_assessment.rst
   data_user_agreement.rst

.. _General Data Protection Regulation: https://ec.europa.eu/info/priorities/justice-and-fundamental-rights/data-protection/2018-reform-eu-data-protection-rules/eu-data-protection-rules_en
.. _Initial GitHub issue: https://github.com/con/open-brain-consent/issues/24
.. _OHBM Hackathon 2019 project: https://github.com/ohbm/hackathon2019/issues/47
.. _Work-in-progress Google document: https://docs.google.com/document/d/1Mfbl4DZAw7MRPjSxIiM5sfYU4gX-pcghgj5M1qb84jg/edit?usp=sharing
.. _COST workshop: https://github.com/CPernet/open-brain-consent/tree/GLiMR-workshop
