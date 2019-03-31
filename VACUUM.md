
# VACUUM - ( tuneBuildTest_C_scale, tuneBuildTest_C_scale_waon)

<img src="VACUUM_banner.png">

<center>VISUAL AUDIO COMPARISION UTILITY <sub>[FOR]</sub> UNDERSTANDING <sub>[AND]</sub> MEASUREMENT</center>
<center>A testing and analysis workflow</center>

<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#VACUUM" data-toc-modified-id="VACUUM-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>VACUUM</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Let's-bring-the-files-in" data-toc-modified-id="Let's-bring-the-files-in-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Let's bring the files in</a></span><ul class="toc-item"><li><span><a href="#Source1-Track--(-&lt;span id='python_0cb2894e7ad54b1ba8156b1ddefd8c1c_135'&gt;&lt;/span&gt;-)" data-toc-modified-id="Source1-Track--(-<span id='python_0cb2894e7ad54b1ba8156b1ddefd8c1c_25'></span>-)-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Source1 Track  ( <span id="python_0cb2894e7ad54b1ba8156b1ddefd8c1c_66"></span> )</a></span><ul class="toc-item"><li><span><a href="#Open-Source1,-get-some-basic-statistics-and-create-a-player" data-toc-modified-id="Open-Source1,-get-some-basic-statistics-and-create-a-player-3.1.1"><span class="toc-item-num">3.1.1&nbsp;&nbsp;</span>Open Source1, get some basic statistics and create a player</a></span></li><li><span><a href="#Let's-take-a-first-look-at-the-file" data-toc-modified-id="Let's-take-a-first-look-at-the-file-3.1.2"><span class="toc-item-num">3.1.2&nbsp;&nbsp;</span>Let's take a first look at the file</a></span></li></ul></li><li><span><a href="#Source-2-Track--(-&lt;span id='python_20ea2a881a80453bb86ba76c5fbd1f6e_138'&gt;&lt;/span&gt;-)" data-toc-modified-id="Source-2-Track--(-<span id='python_20ea2a881a80453bb86ba76c5fbd1f6e_26'></span>-)-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Source 2 Track  ( <span id="python_20ea2a881a80453bb86ba76c5fbd1f6e_68"></span> )</a></span><ul class="toc-item"><li><span><a href="#Open-Source2,-get-some-basic-statistics-and-create-a-player" data-toc-modified-id="Open-Source2,-get-some-basic-statistics-and-create-a-player-3.2.1"><span class="toc-item-num">3.2.1&nbsp;&nbsp;</span>Open Source2, get some basic statistics and create a player</a></span></li><li><span><a href="#Let's-take-a-first-look-at-the-file" data-toc-modified-id="Let's-take-a-first-look-at-the-file-3.2.2"><span class="toc-item-num">3.2.2&nbsp;&nbsp;</span>Let's take a first look at the file</a></span></li></ul></li></ul></li><li><span><a href="#Enhanced-chroma-and-chroma-variants-(source1)" data-toc-modified-id="Enhanced-chroma-and-chroma-variants-(source1)-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Enhanced chroma and chroma variants (source1)</a></span><ul class="toc-item"><li><span><a href="#Original-source1" data-toc-modified-id="Original-source1-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Original source1</a></span></li><li><span><a href="#Correct-Tuning-Deviations" data-toc-modified-id="Correct-Tuning-Deviations-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Correct Tuning Deviations</a></span></li><li><span><a href="#Isolate-harmonic-component" data-toc-modified-id="Isolate-harmonic-component-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Isolate harmonic component</a></span></li><li><span><a href="#Non-local-filtering" data-toc-modified-id="Non-local-filtering-4.4"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>Non-local filtering</a></span></li><li><span><a href="#Horizontal-Median-Filter" data-toc-modified-id="Horizontal-Median-Filter-4.5"><span class="toc-item-num">4.5&nbsp;&nbsp;</span>Horizontal Median Filter</a></span></li><li><span><a href="#Before-and-After" data-toc-modified-id="Before-and-After-4.6"><span class="toc-item-num">4.6&nbsp;&nbsp;</span>Before and After</a></span></li></ul></li><li><span><a href="#Applying-chroma-enchancement-techniques-to-source-files" data-toc-modified-id="Applying-chroma-enchancement-techniques-to-source-files-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Applying chroma enchancement techniques to source files</a></span><ul class="toc-item"><li><span><a href="#Source1" data-toc-modified-id="Source1-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Source1</a></span></li><li><span><a href="#Source2" data-toc-modified-id="Source2-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Source2</a></span></li></ul></li><li><span><a href="#Output-comparisions-for-testing" data-toc-modified-id="Output-comparisions-for-testing-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Output comparisions for testing</a></span></li><li><span><a href="#Run-imageDiff" data-toc-modified-id="Run-imageDiff-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Run imageDiff</a></span></li></ul></div>

# Imports 

    Librosa
    IPython
    Numpy
    Scipy
    Matplotlib

# Let's bring the files in

## Source1 Track  ( tuneBuildTest_C_scale.wav )

### Open Source1, get some basic statistics and create a player

    File: source/tuneBuildTest_C_scale.wav 
    Duration: 8.0000 sec
    Tuning estimate: 0.010000000000000009


### Let's take a first look at the file


![png](VACUUM_files/VACUUM_14_0.png)


## Source 2 Track  ( tuneBuildTest_C_scale_waon.wav )

### Open Source2, get some basic statistics and create a player

    File: source/tuneBuildTest_C_scale_waon.wav 
    Duration: 8.9135 sec
    Tuning estimate: 0.030000000000000027


### Let's take a first look at the file


![png](VACUUM_files/VACUUM_19_0.png)


# Enhanced chroma and chroma variants (source1)
[Enhanced chroma and chroma variants](http://librosa.github.io/librosa/auto_examples/plot_chroma.html#sphx-glr-auto-examples-plot-chroma-py)

## Original source1


![png](VACUUM_files/VACUUM_22_0.png)


## Correct Tuning Deviations


![png](VACUUM_files/VACUUM_24_0.png)


## Isolate harmonic component


![png](VACUUM_files/VACUUM_26_0.png)


## Non-local filtering


![png](VACUUM_files/VACUUM_28_0.png)


## Horizontal Median Filter


![png](VACUUM_files/VACUUM_30_0.png)


## Before and After


![png](VACUUM_files/VACUUM_32_0.png)


# Applying chroma enchancement techniques to source files

## Source1


![png](VACUUM_files/VACUUM_35_0.png)


## Source2


![png](VACUUM_files/VACUUM_37_0.png)


# Output comparisions for testing


![png](VACUUM_files/VACUUM_39_0.png)



![png](VACUUM_files/VACUUM_39_1.png)


# Run imageDiff

    SSIM: 0.6378025534202998



![png](VACUUM_files/VACUUM_42_1.png)

