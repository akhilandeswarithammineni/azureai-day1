response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "you are AI assistant which does only key phrase extraction from the user content separated by commas"},
        {"role": "user", "content": "India is a beautiful country filled with nature and good culture"}
        
    ],
)

print(response.choices[0].message.content)