import click

@click.command()
@click.option('--name', default='Guest', help='要打招呼的人名')
@click.option('--repeat', default=1, help='重复次数')
def main(name, repeat):
    """这是一个使用 Click 生成的简单 CLI 工具"""
    for _ in range(repeat):
        click.echo(f"Hello, {name}!")
    
    # 你之前想运行的 Goodbye 逻辑放在这里
    click.echo("Goodbye from simples __init__ main!")

if __name__ == "__main__":
    main()