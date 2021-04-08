# Letting GPT-3 write my thesis for me

The idea is to make GPT-3 transform unformatted notes (i.e. bullet points) into a scientific text with the same contentas  the notes.
For that, the following pattern was used:
```
# Notes:
<bullet points summarizing a part of a paper>

# Text:
<excerpt of a paper>
```

Concatenating a few of such snippets with the notes I wrote for experiments should make GPT-3 write my master thesis, but only withthings that I actually want to say (it should make up the language, not the content).

# Does it work?
Sometimes yes! It did not work so well when I used less examples, but with the current prompt I got this on second trial:
```
Notes:
- consider audio to audio losses for generative machine learning models
- other authors showed: multi scale spectrogram losses do not provide useful gradients for finding the pitch
- same holds for spectral centroid, even though they have a perfect global loss landscape
- reason: wobbly loss surface  on a small scale makes gradients point into random directions
- aim of this work: find loss function that approximates spectral centroid and has a smooth surface
- if successful, it can be used to train networks to extract pitch

Text:
While previous work has shown that multi-scale spectrogram losses do not provide useful gradients for finding the pitch, we show that the spectral centroid loss is also unsuitable for this task.
In particular, we show that the spectral centroid loss has a wobbly loss surface on a small scale, which makes gradients point into random directions.
We propose a new loss function, the spectral centroid-like loss, which is a smooth approximation of the spectral centroid loss. We show that the spectral centroid-like loss has a smooth loss surface, which
```

So far it has done the following failures:
- started talking about things not mentioned in the notes
- started writing new stuff in the style of bullet points, where I wanted it to write text

# Bibliography of the papers used
- Engel, Jesse, Lamtharn Hantrakul, Chenjie Gu, und Adam Roberts. 2020. „DIFFERENTIABLE DIGITAL SIGNAL PROCESSING“, 19.
- Oord, Aaron van den, Sander Dieleman, Heiga Zen, Karen Simonyan, Oriol Vinyals, Alex Graves, Nal Kalchbrenner, Andrew Senior, und Koray Kavukcuoglu. 2016. „WaveNet: A Generative Model for Raw Audio“. arXiv:1609.03499 [cs], September. http://arxiv.org/abs/1609.03499.
- Turian, Joseph, und Max Henry. 2020. „I’m Sorry for Your Loss: Spectrally-Based Audio Distances Are Bad at Pitch“. arXiv:2012.04572 [cs, eess], Dezember. http://arxiv.org/abs/2012.04572.
- „[2005.14165] Language Models are Few-Shot Learners“. o. J. Zugegriffen 8. April 2021. https://arxiv.org/abs/2005.14165.
