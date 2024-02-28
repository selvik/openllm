import openllm

client = openllm.client.HTTPClient('http://localhost:3000')
answer=client.query('Explain to me the difference between "further" and "farther"')

print(answer)
