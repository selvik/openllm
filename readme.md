Env
- G5.xlarge with DL AMI (2.15 Pytorch) on EC2


Setup the project directory using venv

```
python -m venv openllm
cd openllm/
source .//bin/activate
```

Install Prereqs

```
pip install openllm
pip install --upgrade pip
pip install "openllm[vllm]"
```

Start the model

```
openllm start HuggingFaceH4/zephyr-7b-alpha --quantize int4 --max-model-len 10000
```

Running the client

```
python client.py
```

Output looks like this:
```
$ python client.py
GenerationOutput(prompt='Explain to me the difference between "further" and "farther"', finished=True, outputs=[CompletionChunk(index=0, text=' and how to use each correctly in a sentence. Also, provide me with some examples of when to use each word.\n\nFurther and farther are often confused because they sound similar and have similar meanings. However, they are not interchangeable in all cases.\n\nFurther is used to describe distance in terms of time, space, or degree. It is commonly used in academic, professional, and formal writing.\n\nExamples:\n\n1. The company plans to expand its operations further into Asia.\n2. The deadline for submitting your application is further away than you think.\n3', token_ids=[304, 910, 298, 938, 1430, 12742, 297, 264, 12271, 28723, 4840, 28725, 3084, 528, 395, 741, 9254, 302, 739, 298, 938, 1430, 1707, 28723, 13, 13, 28765, 324, 620, 304, 20936, 460, 2608, 13803, 1096, 590, 2622, 3684, 304, 506, 3684, 2072, 742, 28723, 2993, 28725, 590, 460, 459, 791, 4078, 522, 297, 544, 4469, 28723, 13, 13, 28765, 324, 620, 349, 1307, 298, 6685, 5328, 297, 3471, 302, 727, 28725, 2764, 28725, 442, 6153, 28723, 661, 349, 14473, 1307, 297, 11860, 28725, 5024, 28725, 304, 9907, 3653, 28723, 13, 13, 966, 9874, 28747, 13, 13, 28740, 28723, 415, 2496, 6400, 298, 6710, 871, 6933, 3629, 778, 11065, 28723, 13, 28750, 28723, 415, 25326, 354, 24301, 3257, 574, 4993, 349, 3629, 1753, 821, 368, 1073, 28723, 13, 28770], cumulative_logprob=-50.70559000968933, logprobs=None, finish_reason='length')], prompt_token_ids=[1, 13702, 426, 298, 528, 272, 5133, 1444, 345, 26711, 620, 28739, 304, 345, 15057, 620, 28739], prompt_logprobs=None, request_id='openllm-c0bfc02a317e4a908f4e7cbd93cc1c2c')
```

Build a bento with this:

```
$ openllm build HuggingFaceH4/zephyr-7b-alpha --quantize int4 --max-model-len 10000

```


Convert bento to docker container:

```
$ bentoml containerize huggingfaceh4--zephyr-7b-alpha-service:2ce2d025864af849b3e5029e2ec9d568eeda892d --opt progress=plain
```

Can take a few minutes.
