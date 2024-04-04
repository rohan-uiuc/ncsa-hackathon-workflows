# Hackathon Starter Workflows
 A collection of example workflows to kickstart hackathon projects.

 1. Enron dataset task
 - Enron email dataset in kaggle https://www.kaggle.com/datasets/wcukierski/enron-email-dataset/data . 1.5GB dataset. Not a very clean dataset
 - Parse and clean dataset
 - Tasks :
   * Get the count of user sent emails per year and plot it
   * NetworkX graph from emails
   * RAG pipeline
   * Find the most important person and summarize all the emails

  2. Letterbox dataset
     - Letterboxd dataset is a more cleaner and elaborate IMDb dataset https://www.kaggle.com/datasets/gsimonx37/letterboxd/data
     - Has posters (image data) and multiple csv tabular data
     - Can devise some tasks that might combine multiple data?

3. Kaggle dataset for computer vision
   - https://www.kaggle.com/datasets?tags=13207-Computer+Vision
   - Can pick one task. These datasets will need some preprocessing.

4. Astronomical Image processing workflow
   - Most astronomical deep-sky imagery needs some processing.
   - Multiple images, filters, denoising.
   - Pixinsight is a software that people use to process FITS images https://pixinsight.com/
   - LSST datasets, some tools and some tutorials https://github.com/lsst/dp0-2_lsst_io/tree/main
   - European Org for Astronomical Research Data processing pipeline https://www.eso.org/sci/software/edps.html https://ftp.eso.org/pub/dfs/pipelines/libraries/edps/edps_tutorial0.9.pdf 

5. DocVQA
   - massive dataset of visual docs for QA. https://rrc.cvc.uab.es/?ch=17&com=introduction
   - Can define some tasks based on this dataset
  
 6. RE_MAT project
    - https://github.com/re-mat/clowder-extractors/blob/main/experiment-from-excel/remat.experiment_from_excel.py


# Accessing LLMs 

## 1. NCSA-hosted "best of the open source" models
NCSA has a new project to host LLMs that are directly compatible with the OpenAI API. 

* API Docs: https://docs.ncsa.ai/
* Playground (experimental: no guarentee that all features work): https://ncsa.ai/

## 2. Azure OpenAI API
Come see a hackathon organizer and we can provide Azure OpenAI API keys. These are generously subsidised by Microsoft Research. This has access to GPT-4 Turbo, etc. We only have the Azure version, not the regular OpenAI version.

## 3. Anyscale Endpoints (3rd party)
This is favorite LLM provider, they have a generous free tier, high rate limits, and leading-class features like function calling and json mode. 
You'll have to create your own account. I recommend using the models `Mistral` and `Mixtral`.

* Function calling blog / explainer: https://www.anyscale.com/blog/anyscale-endpoints-json-mode-and-function-calling-features
* Function calling docs: https://docs.endpoints.anyscale.com/text-generation/function-calling
* JSON mode docs: https://docs.endpoints.anyscale.com/text-generation/json-mode/
* OpenAI docs (good to read important notes!): https://platform.openai.com/docs/guides/text-generation/json-mode


