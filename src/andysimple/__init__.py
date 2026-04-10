import click
import sys

@click.group(invoke_without_command=True)
@click.option("--name", default="Guest", help="要打招呼的人名")
@click.option("--repeat", default=1, help="重复次数")
@click.option("-v", "--version", is_flag=True, help="显示版本信息")
@click.option("-i", "--install", is_flag=True, help="安装")
@click.option("-u", "--update", is_flag=True, help="更新")
@click.pass_context  
def main(ctx, name, repeat, version, install, update):
    # 当没有任何选项被触发时，显示帮助信息
    if not (version or install or update):
        # 检查是否传入了 name 或 repeat（即用户是否显式提供了参数）
        # 如果什么都没提供（包括默认值也没被覆盖），则显示帮助
        if ctx.invoked_subcommand is None and len(sys.argv) == 1:
            click.echo(ctx.get_help())
            ctx.exit()

    if ctx.invoked_subcommand is None:
        if version:
            click.echo("andysimple 0.1.2")
        elif install:
            click.echo("安装 andysimple...")
            # 这里可以添加安装逻辑
        elif update:
            click.echo("更新 andysimple...")
            # 这里可以添加更新逻辑
        else:
            for _ in range(repeat):
                click.echo(f"Hello, {name}!")

            # 你之前想运行的 Goodbye 逻辑放在这里
            click.echo("Goodbye from simples __init__ main!")


@main.command()
@click.option("--read", default="", help="读取消息")
@click.option("--write", default="", help="要写入的消息")
def message(read, write):
    """子命令：处理消息读取和写入"""
    if read:
        click.echo(f"Reading message... {read}")
    if write:
        click.echo(f"Writing message: {write}")
    if not read and not write:
        click.echo("请使用 --read 或 --write 之一。")


@main.command()
@click.option("--grant", default="", help="授权")
@click.option("--revoke", default="", help="撤销授权")
def permission(grant, revoke):
    """子命令：处理授权"""
    if grant:
        click.echo(f"Grant {grant}")
    if revoke:
        click.echo(f"Revoke {revoke}")
    if not grant and not revoke:
        click.echo("请使用 --grant 或 --revoke 之一。")


if __name__ == "__main__":
    main()
