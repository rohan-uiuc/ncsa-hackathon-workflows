# Welcome to the 2024 Ashby Prize in Computational Science Hackathon
* [Hackathon general info website](https://ai.ncsa.illinois.edu/news-events/2024/03/2024-ashby-prize-in-computational-science-hackathon/)

## Rules and Judging
1. You can create anything you want but it **must involve computatoinal science**.
2. You will be judgged primarially on innovation, inginuity and creativity, as well as the [other criteria mentioned here](https://ai.ncsa.illinois.edu/news-events/2024/03/2024-ashby-prize-in-computational-science-hackathon/) like your final oral presentation.


# Example Hackathon Starter Workflows
 A loose collection of example workflows to kickstart hackathon projects. Each of these are just starting points that need significant work and focus to make real.

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

## 3. [UIUC.chat](https://www.uiuc.chat/) - RAG llm API 
The UIUC.chat API allows you to upload many types of documents and chat with them. The API will return "answers that are grounded in your documents" much like [Perplexity.ai](https://www.perplexity.ai/).

Please email me (kvday2@illinois.edu) if you have any questions or problems! Just a quick casual, email is great, low pressure.

* UIUC.chat https://www.uiuc.chat/
* API docs: https://docs.uiuc.chat/uiuc.chat-api/api-keys
* Tutorial & highlights: https://www.youtube.com/watch?v=IIMCrIoz7LM&ab_channel=KastanDay

**Usage:**

![CleanShot 2024-04-04 at 15 37 54](https://github.com/rohan-uiuc/ncsa-hackathon-workflows/assets/13607221/63cb31ab-0e10-49d3-82d7-a5cbd05cb394)

1. Make an account with your Illinois email.
2. Create a new project by uploading documents
3. This requires supplying an Azure OpenAI key (see above). Enter it on the **"Materials" page** under **Project-wide OpenAl key** before continuing.
4. Try chatting with your documents on the website, then try via the API.

## 4. Anyscale Endpoints (3rd party)
This is favorite LLM provider, they have a generous free tier, high rate limits, and leading-class features like function calling and json mode. 
You'll have to create your own account. I recommend using the models `Mistral` and `Mixtral`.

* Function calling blog / explainer: https://www.anyscale.com/blog/anyscale-endpoints-json-mode-and-function-calling-features
* Function calling docs: https://docs.endpoints.anyscale.com/text-generation/function-calling
* JSON mode docs: https://docs.endpoints.anyscale.com/text-generation/json-mode/
* OpenAI docs (good to read important notes!): https://platform.openai.com/docs/guides/text-generation/json-mode


