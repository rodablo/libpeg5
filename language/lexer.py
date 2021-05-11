from langkit.lexer import (
    Lexer, LexerToken, TokenFamily, Literal,
    WithText, WithSymbol, WithTrivia,
    Pattern, Ignore, Alt, Case
)


class Token(LexerToken):
    ##

    # Lexical syntax
    # to grammar Identifier	<- 	IdentStart IdentCont* Spacing
   #  Identifier = WithSymbol()
    #IdentStart = WithText()
    # to grammar IdentStart / [0-9]
    #
    Literal = WithText()
    Class = WithText()
    Range = WithText()
    Range2 = WithText()
    #LiteralChar = WithText()
    Char = WithText()

    #
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
    #SQuo = WithText()
    #DQuo = WithText()
    Dash = WithText()

    #
    #Spacing = WithText()
    Comment = WithTrivia()
    #Space = WithText()
    EndOfLine = WithText()
    #EndOfFile = WithText()  # no se si es necesario ver Termination

    Identifier = WithSymbol()
    DefIdentifier = WithSymbol()
    RefIdentifier = WithSymbol()
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
    #('some_char', r'[0-9a-zA-Z]'),
    #('literal', r"'({some_char}|[^\n'])*'"
    #           r'|"({some_char}|[^\n"])*"'),

    ("LITERAL_DBQ", r'"(\\"|[^\n"])*"'),
    ("LITERAL_SQ",  r"'(\\'|[^\n'])*'"),

    #('end_of_line', r"\n|\r"),
    #('bracket_char', r'(\[\"[0-9a-fA-F]+\"\])'),
    #('digit', r"[0-9]"),
    #('range', r"(\[({some_char}-{some_char})?\])"
    #         r"|(\[({some_char})?\])"),
    #('id_start', r"[_a-zA-Z]"),
    #('id_continue', r"([0-9]|{id_start})*"),
    #('id_def', r"{id_start}{id_continue}"),
    ('IDENTIFIER', r"[a-zA-Z_][a-zA-Z0-9_]*")
    #('id_ref', r"{id_def}[^<]"),
    
    
    # https://en.wikipedia.org/wiki/Template:General_Category_(Unicode)
    #('identifier', r"\$?(\p{Lu}|\p{Ll}|\p{Lt}|\p{Lm}|\p{Lo}|\p{Nl}"
    #               r"|{bracket_char})"
    #               r"(\p{Lu}|\p{Ll}|\p{Lt}|\p{Lm}|\p{Lo}|\p{Nl}|\p{Nd}|\p{Mn}"
    #               r"|\p{Mc}"
    #               r"|_|{bracket_char})*"),
)

p5_lexer.add_rules(

    #(Pattern('end_of_line'),    Token.EndOfLine),
    (Literal('\n'),             Token.NL),
    (Pattern(r"[ \r\t]+"),    Ignore()),
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
    #(Literal("'"),              Token.SQuo),
    #(Pattern(r'\"'),             Token.DQuo),
    (Literal("["),              Token.LBra),
    (Literal("]"),              Token.RBra),
    (Literal("-"),          Token.Dash),
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

