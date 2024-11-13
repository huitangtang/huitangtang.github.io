
# 📝 Publications

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/H-SRDC.png"><img src='image/H-SRDC.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<!-- <span class='show_paper_citations' data='eqVvhiQAAAAJ:LkGwnXOMwfcC'></span> // add "| Citations: 11") -->

<b>Towards Uncovering the Intrinsic Data Structures for Unsupervised Domain Adaptation using Structurally Regularized Deep Clustering</b><br>
<i>IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), 2022</i><br>
<b>Hui Tang</b>, Xiatian Zhu, Ke Chen, Kui Jia, and CL Philip Chen<br>
[<a href="https://arxiv.org/pdf/2012.04280">PDF</a>] [<a href="https://github.com/huitangtang/H-SRDC">Code</a>] [<a href="https://huitangtang.github.io/H-SRDC/">Page</a>] [<a href="bibtex/H-SRDC.txt">BibTex</a>]<br>
<div style="text-align: justify">
We are motivated by a Unsupervised domain adaptation (UDA) assumption of structural similarity across domains, 
and propose to directly uncover the intrinsic target discrimination via constrained clustering, 
where we constrain the clustering solutions using structural source regularization that hinges on the very same assumption. 
Technically, we propose a hybrid model of Structurally Regularized Deep Clustering, 
which integrates the regularized discriminative clustering of target data with a generative one, 
and we thus term our method as H-SRDC.
</div>
</div>

</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/DisClusterDA.png"><img src='image/DisClusterDA.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Unsupervised domain adaptation via distilled discriminative clustering</b><br>
<i>Pattern Recognition, 2022</i><br>
<b>Hui Tang</b>, Yaowei Wang, and Kui Jia<br>
[<a href="https://arxiv.org/pdf/2302.11984">PDF</a>] [<a href="https://github.com/huitangtang/DisClusterDA">Code</a>] [<a href="https://huitangtang.github.io/DisClusterDA/">Page</a>] [<a href="bibtex/DisClusterDA.txt">BibTex</a>]<br>
<div style="text-align: justify">
Motivated by the fundamental assumption for domain adaptability, we re-cast the domain adaptation problem as discriminative clustering of target data, 
given strong privileged information provided by the closely related, labeled source data. 
Technically, we use clustering objectives based on a robust variant of entropy minimization that adaptively filters target data, 
a soft Fisher-like criterion, and additionally the cluster ordering via centroid classification. 
To distill discriminative source information for target clustering, we propose to jointly train the network using parallel, supervised learning objectives over labeled source data. 
</div>
</div>

</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/ViCatDA.png"><img src='image/ViCatDA.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Vicinal and categorical domain adaptation</b><br>
<i>Pattern Recognition, 2021</i><br>
<b>Hui Tang</b> and Kui Jia<br>
[<a href="https://arxiv.org/pdf/2103.03460">PDF</a>] [<a href="https://github.com/huitangtang/ViCatDA">Code</a>] [<a href="https://huitangtang.github.io/ViCatDA/">Page</a>] [<a href="bibtex/ViCatDA.txt">BibTex</a>]<br>
<div style="text-align: justify">
To promote categorical domain adaptation (CatDA), based on a joint category-domain classifier, 
we propose novel losses of adversarial training at both domain and category levels. 
Since the joint classifier can be regarded as a concatenation of individual task classifiers respectively for the two domains, 
our design principle is to enforce consistency of category predictions between the two task classifiers. 
Moreover, we propose a concept of vicinal domains whose instances are produced by a convex combination of pairs of instances respectively from the two domains. 
Intuitively, alignment of the possibly infinite number of vicinal domains enhances that of original domains.
</div>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/McDalNets.png"><img src='image/McDalNets.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Unsupervised Multi-Class Domain Adaptation: Theory, Algorithms, and Practice</b><br>
<i>IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), 2022</i><br>
Yabin Zhang, Bin Deng, <b>Hui Tang</b>, Lei Zhang, and Kui Jia<br>
[<a href="https://arxiv.org/pdf/2002.08681">PDF</a>] [<a href="https://github.com/Gorilla-Lab-SCUT/MultiClassDA">Code</a>] [<a href="bibtex/McDalNets.txt">BibTex</a>]<br>
<div style="text-align: justify">
Suggested by a new domain adaptation bound for unsupervised multi-class domain adaptation (multi-class UDA), 
we develop an algorithmic framework of Multi-class Domain-adversarial learning Networks (McDalNets), 
and its different instantiations via surrogate learning objectives either coincide with or resemble a few recently popular methods. 
Based on our identical theory for multi-class UDA, we also introduce a new algorithm of Domain-Symmetric Networks (SymmNets), 
which is featured by a novel adversarial strategy of domain confusion and discrimination.
</div>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/S2RDA.png"><img src='image/DMN.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Dual Memory Networks: A Versatile Adaptation Approach for Vision-Language Models</b><br>
<i>IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2024</i><br>
Yabin Zhang, Wenjie Zhu, <b>Hui Tang</b>, Zhiyuan Ma, Kaiyang Zhou, and Lei Zhang<br>
[<a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Zhang_Dual_Memory_Networks_A_Versatile_Adaptation_Approach_for_Vision-Language_Models_CVPR_2024_paper.pdf">PDF</a>] [<a href="https://github.com/YBZh/DMN">Code</a>] [<a href="bibtex/DMN.txt">BibTex</a>]<br>
<div style="text-align: justify">
To address the limitations of existing approaches that focus solely on single visual-language model adaptation paradigm, we propose a versatile adaptation method that simultaneously accommodates three key settings: zero-shot, few-shot, and training-free few-shot. Using static and dynamic memory networks to extract insights from labeled training and historical test data, our adaptive classifiers convert test features into desired outputs. Validated across 11 datasets, our method achieves a 3% improvement over competitors and outperforms those using external training data in zero-shot scenarios.
</div>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/S2RDA.png"><img src='image/S2RDA.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>A New Benchmark: On the Utility of Synthetic Data with Blender for Bare Supervised Learning and Downstream Domain Adaptation</b><br>
<i>IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2023</i><br>
<b>Hui Tang</b> and Kui Jia<br>
[<a href="https://arxiv.org/pdf/2303.09165">PDF</a>] [<a href="https://github.com/huitangtang/On_the_Utility_of_Synthetic_Data">Code</a>] [<a href="https://huitangtang.github.io/On_the_Utility_of_Synthetic_Data/">Page</a>] [<a href="https://cove.thecvf.com/datasets/892">Dataset</a>] [<a href="bibtex/S2RDA.txt">BibTex</a>]<br>
<div style="text-align: justify">
To solve the basic and important problems in the context of image classification, such as the lack of comprehensive synthetic data research and the insufficient exploration of synthetic-to-real transfer, we propose to exploit synthetic datasets to explore questions on model generalization, benchmark pre-training strategies for domain adaptation (DA), and <i>build a large-scale benchmark dataset S2RDA for synthetic-to-real transfer</i>, which can push forward future DA research.
</div>

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/STOCO.png"><img src='image/STOCO.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Stochastic Consensus: Enhancing Semi-Supervised Learning with Consistency of Stochastic Classifiers</b><br>
<i>European Conference on Computer Vision (ECCV), 2022</i><br>
<b>Hui Tang</b>, Lin Sun, and Kui Jia<br>
[<a href="https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136910319.pdf">PDF</a>] [<a href="https://github.com/huitangtang/STOCO">Code</a>] [<a href="https://huitangtang.github.io/STOCO/">Page</a>] [<a href="bibtex/STOCO.txt">BibTex</a>]<br>
<div style="text-align: justify">
We propose a new criterion based on consistency among multiple, stochastic classifiers, termed Stochastic Consensus (STOCO). 
Specifically, we model parameters of the classifiers as a Gaussian distribution whose mean and standard deviation are jointly optimized during training. 
We technically generate pseudo labels using a simple but flexible framework of deep discriminative clustering.
</div>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/GSF&PPF.png"><img src='image/GSF&PPF.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Towards Discovering the Effectiveness of Moderately Confident Samples for Semi-Supervised Learning</b><br>
<i>IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2022</i><br>
<b>Hui Tang</b> and Kui Jia<br>
[<a href="https://openaccess.thecvf.com/content/CVPR2022/papers/Tang_Towards_Discovering_the_Effectiveness_of_Moderately_Confident_Samples_for_Semi-Supervised_CVPR_2022_paper.pdf">PDF</a>] [<a href="https://github.com/huitangtang/GSF-PPF">Code</a>] [<a href="https://huitangtang.github.io/GSF-PPF/">Page</a>] [<a href="bibtex/GSF&PPF.txt">BibTex</a>]<br>
<div style="text-align: justify">
We propose to utilize moderately confident samples. 
Based on the principle of local optimization landscape consistency, we propose Taylor expansion inspired filtration framework, 
relying on the Taylor expansion of the loss function to inspire the key measurement index of sample filtration, i.e., gradient and feature of finite orders. 
We derive two novel filters from this framework: gradient synchronization filter selecting samples with similar optimization dynamics to the most reliable one, 
and prototype proximity filter selecting samples near semantic prototypes.
</div>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/GAST.png"><img src='image/GAST.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Geometry-Aware Self-Training for Unsupervised Domain Adaptation on Object Point Clouds</b><br>
<i>IEEE/CVF International Conference on Computer Vision (ICCV), 2021</i><br>
Longkun Zou, <b>Hui Tang</b>, Ke Chen, and Kui Jia<br>
[<a href="https://openaccess.thecvf.com/content/ICCV2021/papers/Zou_Geometry-Aware_Self-Training_for_Unsupervised_Domain_Adaptation_on_Object_Point_Clouds_ICCV_2021_paper.pdf">PDF</a>] [<a href="https://github.com/zou-longkun/GAST">Code</a>] [<a href="bibtex/GAST.txt">BibTex</a>]<br>
<div style="text-align: justify">
We propose a novel Geometry-Aware Self-Training (GAST) method for unsupervised domain adaptation on object point sets, 
which encodes domain-invariant geometrics to semantic representation to mitigate domain discrepancy of point-based representations. 
Technically, based on self-paced self-training on unlabeled target data, our GAST integrates the self-supervised tasks of predicting rotation class and distortion location into representation learning, such that the domain-shared feature space can be constructed.
</div>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/SRDC.png"><img src='image/SRDC.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Unsupervised Domain Adaptation via Structurally Regularized Deep Clustering</b><br>
<i>IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), <span style="color:red">Oral Presentation</span>, 2020</i><br>
<b>Hui Tang</b>, Ke Chen, and Kui Jia<br>
[<a href="https://openaccess.thecvf.com/content_CVPR_2020/papers/Tang_Unsupervised_Domain_Adaptation_via_Structurally_Regularized_Deep_Clustering_CVPR_2020_paper.pdf">PDF</a>] [<a href="https://github.com/Gorilla-Lab-SCUT/SRDC-CVPR2020">Code</a>] [<a href="https://huitangtang.github.io/SRDC-CVPR2020/">Page</a>] [<a href="bibtex/SRDC.txt">BibTex</a>]<br>
<div style="text-align: justify">
To address a potential issue of damaging the intrinsic data discrimination by explicitly learning domain-aligned features, 
we propose a source-regularized, deep discriminative clustering method 
in order to directly uncover the intrinsic discrimination among target data, 
termed as Structurally Regularized Deep Clustering (SRDC). 
In SRDC, we also design useful ingredients to enhance target discrimination with clustering of intermediate network features, 
and to enhance structural regularization with soft selection of less divergent source examples.
</div>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/DADA.png"><img src='image/DADA.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Discriminative Adversarial Domain Adaptation</b><br>
<i>AAAI Conference on Artificial Intelligence (AAAI), 2020</i><br>
<b>Hui Tang</b> and Kui Jia<br>
[<a href="https://ojs.aaai.org/index.php/AAAI/article/download/6054/5910">PDF</a>] [<a href="https://github.com/Gorilla-Lab-SCUT/DADA-AAAI2020">Code</a>] [<a href="https://huitangtang.github.io/DADA-AAAI2020/">Page</a>] [<a href="bibtex/DADA.txt">BibTex</a>]<br>
<div style="text-align: justify">
We propose a novel adversarial learning method termed Discriminative Adversarial Domain Adaptation (DADA). 
Based on an integrated category and domain classifier, DADA has a novel adversarial objective that 
encourages a mutually inhibitory relation between category and domain predictions for any input instance. 
Except for the traditional closed set domain adaptation, we also extend DADA for extremely challenging problem settings of partial and open set domain adaptation.
</div>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/SymNet.png"><img src='image/SymNet.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Domain-Symmetric Networks for Adversarial Domain Adaptation</b><br>
<i>IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2019</i><br>
Yabin Zhang, <b>Hui Tang</b>, Kui Jia, and Mingkui Tan<br>
[<a href="https://openaccess.thecvf.com/content_CVPR_2019/papers/Zhang_Domain-Symmetric_Networks_for_Adversarial_Domain_Adaptation_CVPR_2019_paper.pdf">PDF</a>] [<a href="https://github.com/Gorilla-Lab-SCUT/SymNets">Code</a>] [<a href="bibtex/SymNet.txt">BibTex</a>]<br>
<div style="text-align: justify">
We propose a new domain adaptation method called Domain-Symmetric Networks (SymNets). 
The proposed SymNet is based on a symmetric design of source and target task classifiers, 
based on which we also construct an additional classifier that shares with them its layer neurons. 
To train the SymNet, we propose a novel adversarial learning objective 
whose key design is based on a two-level domain confusion scheme.
</div>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/MetaFGNet.png"><img src='image/MetaFGNet.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Fine-Grained Visual Categorization using Meta-Learning Optimization with Sample Selection of Auxiliary Data</b><br>
<i>European Conference on Computer Vision (ECCV), 2018</i><br>
Yabin Zhang, <b>Hui Tang</b>, and Kui Jia<br>
[<a href="https://openaccess.thecvf.com/content_ECCV_2018/papers/Yabin_Zhang_Fine-Grained_Visual_Categorization_ECCV_2018_paper.pdf">PDF</a>] [<a href="https://github.com/Gorilla-Lab-SCUT/MetaFGNet">Code</a>] [<a href="bibtex/MetaFGNet.txt">BibTex</a>]<br>
<div style="text-align: justify">
We propose a new deep fine-grained visual categorization (FGVC) model termed MetaFGNet.
Training of MetaFGNet is based on a novel regularized meta-learning objective, 
which aims to guide the learning of network parameters 
so that they are optimal for adapting to the target FGVC task. 
Based on MetaFGNet, we also propose a simple yet effective scheme for selecting more useful samples from the auxiliary data.
</div>

</div>
</div>
