def mensagem(msg):
    message = f"   {msg}   "
    total_width = int(len(message)/2)
    print("-=" * total_width)
    print(message)
    print("-=" * total_width)
    print()


mensagem("Olá mundo.")
mensagem("Boas galera.")
mensagem("Oi")