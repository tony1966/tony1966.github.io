# hello.py
def main(request):
    name=request.args.get('name', 'World')
    return f'Hello {name}!'
