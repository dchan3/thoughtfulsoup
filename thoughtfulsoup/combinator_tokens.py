COMBINATOR_TOKENS = {
    ">": lambda tag: tag.children, # Run the next token as a CSS selector against the direct children of each tag in the current context.
    '~': lambda tag: tag.next_siblings,  # Run the next token as a CSS selector against the siblings of each tag in the current context.
    '+': lambda tag: (yield tag.find_next_sibling(True)), # For each tag in the current context, run the next token as a CSS selector against the tag's next sibling that's a tag.
}
