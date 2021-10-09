from langkit.lexer import (
    Lexer, LexerToken, TokenFamily, 
    WithText, WithSymbol, WithTrivia,
    Literal, Pattern, Ignore
    # , Alt, Case
    )


class Token(LexerToken):

    Literal = WithText()
    Char = WithText()
    LeftArrow = WithText()
    Slash = WithText()
    And = WithText()
    Not = WithText()
    Question = WithText()
    Star = WithText()
    Plus = WithText()
    LPar = WithText()
    RPar = WithText()
    LBra = WithText()
    RBra = WithText()
    Dot = WithText()
    # SQuo = WithText()
    # DQuo = WithText()
    Dash = WithText()
    Comment = WithTrivia()
    EndOfLine = WithText()

    Identifier = WithSymbol()
    #DefIdentifier = WithSymbol()
    #RefIdentifier = WithSymbol()
    NL = WithText()
    #Identifier = WithText()
    #IdentifierContinue = WithText()
    #
    #Punctuations = TokenFamily(
    #    LeftArrow, Slash, And, Not, Question, Star,
    #    Plus, LPar, RPar, Dot
    #)

p5_lexer = Lexer(Token, 
                 track_indent=False, 
                 pre_rules=[
                    (Pattern(r'\\\n[ \r\t]*'), Ignore())
                 ])

p5_lexer.add_patterns(
    ("LITERAL_DBQ", r'"(\\"|[^\n"])*"'),
    ("LITERAL_SQ",  r"'(\\'|[^\n'])*'"),
    ('IDENTIFIER', r"[a-zA-Z_][a-zA-Z0-9_]*")
    # https://en.wikipedia.org/wiki/Template:General_Category_(Unicode)
    # ('identifier', r"\$?(\p{Lu}|\p{Ll}|\p{Lt}|\p{Lm}|\p{Lo}|\p{Nl}"
    #               r"|{bracket_char})"
    #               r"(\p{Lu}|\p{Ll}|\p{Lt}|\p{Lm}|\p{Lo}|\p{Nl}|\p{Nd}|\p{Mn}"
    #               r"|\p{Mc}"
    #               r"|_|{bracket_char})*"),
)

p5_lexer.add_rules(
    (Literal('\n'),             Token.NL),
    (Pattern(r"[ \r\t]+"),      Ignore()),
    (Pattern(r"#(.?)+"),        Token.Comment),
    (Literal("<-"),             Token.LeftArrow),
    (Literal("/"),              Token.Slash),
    (Literal("&"),              Token.And),
    (Literal("!"),              Token.Not),
    (Literal("?"),              Token.Question),
    (Literal("*"),              Token.Star),
    (Literal("+"),              Token.Plus),
    (Literal("("),              Token.LPar),
    (Literal(")"),              Token.RPar),
    (Literal("."),              Token.Dot),
    # todo: evaluate quoting as tokens
    #(Literal("'"),              Token.SQuo),
    #(Pattern(r'\"'),             Token.DQuo),
    (Literal("["),              Token.LBra),
    (Literal("]"),              Token.RBra),
    (Literal("-"),              Token.Dash),
    #(Pattern('{literal}'),      Token.Literal),
    (Pattern('({LITERAL_SQ}|{LITERAL_DBQ})'),   Token.Literal),

    (Pattern(r"\\[0-2][0-7][0-7]"), Token.Char),

    #(Pattern(r"{some_char}-{some_char}|{some_char}"), Token.Range),
    #(Pattern(r"\[({some_char}-{some_char})*\]"), Token.Range2),
    #(Pattern(r"\[({some_char})*\]"), Token.Range),

    # order of clauses is relevant... 
    #(Pattern('{literal_chars}'),    Token.LiteralChar),

    (Pattern('{IDENTIFIER}'), Token.Identifier),
    #(Pattern('{id_ref}'), Token.RefIdentifier),

    #Case(Literal("a"),
    #    Alt(prev_token_cond=(Token.SQuo, Token.DQuo, Token.LBra, Token.Char), 
    #        send=Token.Char,
    #        match_size=1),
    #    #
    #    Alt(prev_token_cond=(Token.IdentifierStart, Token.IdentifierContinue),
    #        send=Token.IdentifierContinue,
    #        match_size=1),
    #    # last
    #    Alt(send=Token.IdentifierStart,
    #        match_size=1)
    #),

    #(Pattern('{id_continue}'),      Token.IdentifierContinue)
)
