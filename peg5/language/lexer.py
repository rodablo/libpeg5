from langkit.lexer import (Lexer, LexerToken, WithText, WithSymbol, WithTrivia, Literal, Pattern, Ignore,
                           TokenFamily, Alt, Case
                           )


class Token(LexerToken):
    # 
    LeftArrow = WithText()
    Slash = WithText()
    BackSlash = WithText()
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
    Quote = WithText()
    Dash = WithText()
    #
    Literal = WithText()
    #
    Char = WithText()
    Escaped = WithText()
    Octal = WithText()
    #
    Comment = WithTrivia()
    EndOfLine = WithText()
    #Suffix = WithText()
    Identifier = WithSymbol()
    NL = WithText()
    #Identifier = WithText()
    #IdentifierContinue = WithText()
    #
    #Punctuations = TokenFamily(
    #    LeftArrow, Slash, And, Not, Question, Star,
    #    Plus, LPar, RPar, Dot
    #)


p5_lexer = Lexer(Token
    #,
    #track_indent=False,
    #pre_rules=[
    #    (Pattern(r'\\\n[ \r\t]*'), Ignore())
    #]
)

p5_lexer.add_patterns(
    ('ID_CAR', r"[a-zA-Z_]"),
    ('ID_CDR', r"[a-zA-Z0-9_]*"),
#    ('IDENTIFIER', r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ('IDENTIFIER', r"{ID_CAR}{ID_CDR}"),
    #("LITERAL_DBQ", r'"(\\"|[^\n"])*"'),
#    ('CHAR', r"[^'\\\n]"),
    ('OCTAL_CHAR', r"(\\([0-2][0-7][0-7]|[0-7][0-7]?))"),
    ('ESCAPED_CHAR', r"(\\(r|t|n|\\))"),
    ('CHAR', r"({ESCAPED_CHAR}|{OCTAL_CHAR}|[^\n])"),
    ("LITERAL_S", r"('({CHAR}|\")*')"),
    ("LITERAL_D", r'("({CHAR}|\')*")'),
    ("LITERAL", r"({LITERAL_S}|{LITERAL_D})"),

#    ('ESCAPE_2_CHAR', r"«"),
#    ('CHAR', r"(({ESCAPE_1_CHAR}|{ESCAPE_2_CHAR}))"),

    # https://en.wikipedia.org/wiki/Template:General_Category_(Unicode)
    # ('identifier', r"\$?(\p{Lu}|\p{Ll}|\p{Lt}|\p{Lm}|\p{Lo}|\p{Nl}"
    #               r"|{bracket_char})"
    #               r"(\p{Lu}|\p{Ll}|\p{Lt}|\p{Lm}|\p{Lo}|\p{Nl}|\p{Nd}|\p{Mn}"
    #               r"|\p{Mc}"
    #               r"|_|{bracket_char})*"),
    #TODO: this needs to be tokenized too.... az.\n\t
)


rules = [
    (Literal('\n'), Token.NL),
    (Pattern(r"[ \r\t]+"), Ignore()),
]

non_esc_chr = "'\\\\\n"

#rules.append(
#    Case(
#        Pattern(r"[a-zA-Z_]"),
#        Alt(prev_token_cond=(Token.Quote, Token.Literal, Token.Char),
#            send=Token.Char, match_size=1),
#        Alt(send=Token.Identifier, match_size=1)
#    )
#)

#rules.append(
#    Case(
#        Literal("\\"),
#        Alt(prev_token_cond=(Token.Quote, Token.Literal, Token.Char),
#            send=Token.Escape, match_size=1),
#        Alt(prev_token_cond=(Token.Escape, ),
#            send=Token.Literal, match_size=1),
#        Alt(send=Token.BackSlash, match_size=1)
#    )
#)


for txt, esc, tok in [
#    ("\\", r"\\", Token.BackSlash),
    ("/", "/", Token.Slash),
    ("&", r"\&", Token.And),
    ("!", r"\!", Token.Not),
    ("*", r"\*", Token.Star),
    ("?", r"\?", Token.Question),
    ("+", r"\+", Token.Plus),
    ("(", r"\(", Token.LPar),
    (")", r"\)", Token.RPar),
    (".", r"\.", Token.Dot),
    ("[", r"\[", Token.LBra),
    ("]", r"\]", Token.RBra),
    ("-", r"\-", Token.Dash),
]:
    rules.append(
        Case(
            Literal(txt),
            Alt(prev_token_cond=(Token.Quote, Token.Literal, Token.Char, Token.BackSlash),
                send=Token.Char, match_size=len(txt)),
            Alt(send=tok, match_size=len(txt))
        )
    )
    non_esc_chr += esc
    #print('{}->{}'.format(txt, tok))

toto = "[^{}]+".format(non_esc_chr)
# print(toto)
#p5_lexer.add_patterns(
#    ('NON_ESCAPED_CHARS', toto),
#)
#Case(
#    Pattern(r"a+"),
#    Alt(prev_token_cond=(Token.Quote, Token.Literal),
#        send=Token.Literal, match_size=1),
#    Alt(send=Token.Suffix, match_size=1)
#)

rules += [
    #
    (Literal("<-"), Token.LeftArrow),
    (Literal("'"), Token.Quote),
#    (Literal("\\"), Token.BackSlash),
#    (Literal("/"), Token.Slash),
#    (Literal("&"), Token.And),
#    (Literal("!"), Token.Not),
#    (Literal("?"), Token.Question),
#    (Literal("*"), Token.Star),
#    (Literal("+"), Token.Plus),
#    (Literal("("), Token.LPar),
#    (Literal(")"), Token.RPar),
#    (Literal("."), Token.Dot),
#    # todo: evaluate quoting as tokens
#    #(Literal("'"),              Token.SQuo),
#    #(Pattern(r'\"'),             Token.DQuo),
#    (Literal("["), Token.LBra),
#    (Literal("]"), Token.RBra),
#    (Literal("-"), Token.Dash),
    #(Pattern('{literal}'),      Token.Literal),
    #(Pattern('({LITERAL_SQ}|{LITERAL_DBQ})'), Token.Literal),
    (Pattern('{LITERAL}'), Token.Literal),
    (Pattern('{CHAR}'), Token.Char),
    (Pattern('{IDENTIFIER}'), Token.Identifier),

    #(Pattern('{OCTAL_CHAR}'), Token.Octal),
    #(Pattern('{ESCAPED_CHAR}'), Token.Escaped),

    # order of clauses is relevant...
    #(Pattern('{literal_chars}'),    Token.LiteralChar),

    #(Pattern('{id_ref}'), Token.RefIdentifier),

#    (Pattern('{NON_ESCAPED_CHARS}'), Token.Literal),
    (Pattern(r"#(.?)+"), Token.Comment),

]


p5_lexer.add_rules(*rules)
