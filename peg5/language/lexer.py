from langkit.lexer import (
    Lexer, LexerToken, WithText, WithSymbol, WithTrivia, Literal, Pattern,
    # Ignore, TokenFamily, Alt, Case
)


class Token(LexerToken):
    #
    LeftArrow = WithText()
    Slash = WithText()
    #BackSlash = WithText()
    And = WithText()
    Not = WithText()
    Star = WithText()
    Plus = WithText()
    Question = WithText()
    LPar = WithText()
    RPar = WithText()
    #LBra = WithText()
    #RBra = WithText()
    Dot = WithText()
    #Quote = WithText()
    #Dash = WithText()
    #TODO: temporary hack until i fully undertand how to make <- left associative
    Semicolon = WithText()
    #
    Literal = WithText()
    #
    #Char = WithText()
    #Escaped = WithText()
    #Octal = WithText()
    UnaryRangeClass = WithText()
    BinaryRangeClass = WithText()
    #
    #EndOfLine = WithText()
    #Suffix = WithText()
    Identifier = WithSymbol()
    #NL = WithText()
    #Identifier = WithText()
    #IdentifierContinue = WithText()
    #
    Comment = WithTrivia()
    Whitespace = WithTrivia()

    #Punctuations = TokenFamily(
    #    LeftArrow, Slash, And, Not, Question, Star,
    #    Plus, LPar, RPar, Dot
    #)


peg5_lexer = Lexer(Token)

peg5_lexer.add_patterns(
    ('ID_CAR', r"[a-zA-Z_]"),
    ('ID_CDR', r"({ID_CAR}|[0-9])*"),
    ('IDENTIFIER', r"{ID_CAR}{ID_CDR}"),
    ('OCTAL_CHAR', r"(\\([0-2][0-7][0-7]|[0-7][0-7]?))"),
    ('ESCAPED_CHAR', r"(\\[rtn\\])"),
    ('CHAR', r"({ESCAPED_CHAR}|{OCTAL_CHAR}|[^\n])"),
    ("LITERAL_S", r"('({CHAR}|\")*')"),
    ("LITERAL_D", r'("({CHAR}|\')*")'),
    ("LITERAL", r"({LITERAL_S}|{LITERAL_D})"),
    ("CLASS_U", r"(\[{CHAR}\])"),
    ("CLASS_B", r"(\[{CHAR}-{CHAR}\])"),

    # https://en.wikipedia.org/wiki/Template:General_Category_(Unicode)
    # ('identifier', r"\$?(\p{Lu}|\p{Ll}|\p{Lt}|\p{Lm}|\p{Lo}|\p{Nl}"
    #               r"|{bracket_char})"
    #               r"(\p{Lu}|\p{Ll}|\p{Lt}|\p{Lm}|\p{Lo}|\p{Nl}|\p{Nd}|\p{Mn}"
    #               r"|\p{Mc}"
    #               r"|_|{bracket_char})*"),
)


rules = [
    # Blanks and trivia
    (Pattern(r"[ \t\r\n\f]+"), Token.Whitespace),
    (Pattern(r"#(.?)+"), Token.Comment),
]

#non_esc_chr = "'\\\\\n"

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


#for txt, esc, tok in [
#    ("/", "/", Token.Slash),
#    ("&", r"\&", Token.And),
#    ("!", r"\!", Token.Not),
#    ("*", r"\*", Token.Star),
#    ("?", r"\?", Token.Question),
#    ("+", r"\+", Token.Plus),
#    ("(", r"\(", Token.LPar),
#    (")", r"\)", Token.RPar),
#    (".", r"\.", Token.Dot),
#    ("[", r"\[", Token.LBra),
#    ("]", r"\]", Token.RBra),
#    ("-", r"\-", Token.Dash),
#    (";", ";", Token.Semicolon),
#]:
#    rules.append(
#        (Literal(txt), tok)
#        #        Case(
#        #            Literal(txt),
#        #            Alt(prev_token_cond=(Token.Quote, Token.Literal, Token.Char, Token.BackSlash),
#        #                send=Token.Char, match_size=len(txt)),
#        #            Alt(send=tok, match_size=len(txt))
#        #        )
#    )
#    non_esc_chr += esc
#   #print('{}->{}'.format(txt, tok))
##peg5_lexer.add_patterns(
#    ('NON_ESCAPED_CHARS', "[^{}]+".format(non_esc_chr)),
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
    (Literal("/"), Token.Slash),
    (Literal("&"), Token.And),
    (Literal("!"), Token.Not),
    (Literal("*"), Token.Star),
    (Literal("+"), Token.Plus),
    (Literal("?"), Token.Question),
    (Literal("("), Token.LPar),
    (Literal(")"), Token.RPar),
    (Literal("."), Token.Dot),
    (Literal(";"), Token.Semicolon),

    (Pattern('{IDENTIFIER}'), Token.Identifier),
    (Pattern('{LITERAL}'), Token.Literal),
    #(Pattern('{CHAR}'), Token.Char),

    (Pattern('{CLASS_U}'), Token.UnaryRangeClass),
    (Pattern('{CLASS_B}'), Token.BinaryRangeClass),
    (Pattern(r"#(.?)+"), Token.Comment),
]


peg5_lexer.add_rules(*rules)
