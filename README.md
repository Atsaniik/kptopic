[![PyPI - Python](https://img.shields.io/badge/python-v3.7+-blue.svg)](https://pypi.org/project/kptopic/)
[![docs](https://img.shields.io/badge/docs-Passing-green.svg)](https://github.com/pengKiina/KPTopic/)
[![PyPI - PyPi](https://img.shields.io/pypi/v/kptopic)](https://pypi.org/project/kptopic/)
[![PyPI - License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/pengKiina/KPTopic/blob/main/LICENSE)



# KPTopic
<img src="https://github.com/Atsaniik/kptopic/blob/main/images/kptLogo.png" width="40%" height="20%" align="right" />

*  No more Topic Modeling
*  No need Training 
*  Text Big + Small
*  Emoji + Sentiment Score 

KPTopic: a graph-based approach to represent perception (text in general) by key parts of speech. KPTopic solved the coherence crux that current topic modeling algorithms are trying to deal with but failed. KPTopic extracts the topics from text corpus syntactically, semantically and pragmatically instead of a meaningless combination of words from topic modeling.


## Key Parts: Noun, Adjective, Verb and Emoji 

KPTopic result from the following sentence:

``` “Finland also has beautiful lakes , traditional Sauna, we especially love the Sauna and 🎅 ,   we will definitely come to Finland again.” ```

* KPTopic Result 

<img style="border:1px solid black"
src="https://github.com/Atsaniik/kptopic/blob/main/images/sentence_network.png" width="80%" height="80%" align="center" />


## Installation

```bash
 # pip install kptopic
 # pip install git+https://github.com/Atsaniik/kptopic.git  
```


## Getting Started
For an in-depth overview of the features of KPTopic
you can check the [**Documents**](https://medium.com/@egalitrans/topic-modeling-is-dad-long-live-kptopic-a1998a94a0b0) or you can follow along 
with one of the examples as follows:

| Name  | Link  |
|---|---|
| KPTopic Quick Start | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1wojipc1hdPh4ubQ05s_vHUm7S6HZhjkn?usp=sharing) |

## Visualization Examples 
* 1 Community Construction 

The following is one of the communities generated from a example of corpus comprised of reviews by those who visit Finland.

<img src="https://github.com/Atsaniik/kptopic/blob/main/images/community%20image.png" width="90%" height="90%" align="center" />

* 2 Topic Generated 

The following topic is generated from the community network.

<img src="https://github.com/Atsaniik/kptopic/blob/main/images/topic_AI.png" width="90%" height="35%" align="center" />

* 3 Key Parts of Speech 

<img src="https://github.com/Atsaniik/kptopic/blob/main/images/keyparts.png" width="90%" height="50%" align="center" />

* 4 Sentiment Distribution
<img src="https://github.com/Atsaniik/kptopic/blob/main/images/sentiment.png" width="80%" height="50%" align="center" />



## Citation
To cite the [KPTopic paper](https://arxiv.org/abs/29.11844), please use the following bibtex reference:

```bibtext
@article{pengyang,
  title={KPTopic},
  author={Peng, Yang},
  journal={a1},
  year={202}
}
```





