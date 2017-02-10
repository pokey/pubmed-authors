# -*- coding: utf-8 -*-

import asyncio

import click

from pubmed_authors import run


@click.command()
@click.argument('terms', nargs=-1)
def main(terms):
    """Console script for pubmed_authors"""
    query = ' '.join(terms)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(query))
    loop.close()


if __name__ == "__main__":
    main()
