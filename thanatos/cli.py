#!/usr/bin/env python
""" Command line access for thanatos """

import logging
import argparse

import thanatos


def main():
    parser = argparse.ArgumentParser(
        description=(
            """A command line interface for the Thanatos library. This can """
            """be used to populate a database with the required EVE Online """
            """static data or for generating random EVE trivia questions."""
        ),
    )
    
    parser.add_argument('-t', '--list_tables', action='store_true',
                        help='Lists all the SDE tables required by Thanatos.')
    
    parser.add_argument('-d', '--download_tables', action='store_true',
                        help='Downloads all tables required by Thanatos.')
    
    parser.add_argument('-l', '--loglevel', type=str,
                        help='Enable logging of messages at or above the provided level.')

    args = parser.parse_args()
        
    if args.loglevel is not None:
        log_level    = getattr(logging, args.loglevel)
        thanatos_log = logging.getLogger('thanatos')
        log_handler  = logging.StreamHandler()
        
        log_handler.setLevel(log_level)
        thanatos_log.setLevel(log_level)
        thanatos_log.addHandler(log_handler)
    
    if args.list_tables:
        thanatos.database.required_tables
    
    if args.download_tables:
        thanatos.utils.download_tables(thanatos.database.required_tables)

    if args.setup_tables:
        pass

if __name__ == "__main__":
    main()