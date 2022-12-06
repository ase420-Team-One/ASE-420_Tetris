import pygame


class TkPygameInterpreter:
    _tk_to_pygame_dict = {
        22: pygame.K_BACKSPACE,
        23: pygame.K_TAB,
        110: pygame.K_PAUSE,
        9: pygame.K_ESCAPE,
        32: pygame.K_SPACE,
        44: pygame.K_COMMA,
        46: pygame.K_PERIOD,
        47: pygame.K_SLASH,
        45: pygame.K_MINUS,
        48: pygame.K_0,
        49: pygame.K_1,
        50: pygame.K_2,
        51: pygame.K_3,
        52: pygame.K_4,
        53: pygame.K_5,
        54: pygame.K_6,
        55: pygame.K_7,
        56: pygame.K_8,
        57: pygame.K_9,
        59: pygame.K_SEMICOLON,
        61: pygame.K_EQUALS,
        91: pygame.K_LEFTBRACKET,
        92: pygame.K_BACKSLASH,
        93: pygame.K_RIGHTBRACKET,
        65: pygame.K_a,
        66: pygame.K_b,
        67: pygame.K_c,
        68: pygame.K_d,
        69: pygame.K_e,
        70: pygame.K_f,
        71: pygame.K_g,
        72: pygame.K_h,
        73: pygame.K_i,
        74: pygame.K_j,
        75: pygame.K_k,
        76: pygame.K_l,
        77: pygame.K_m,
        78: pygame.K_n,
        79: pygame.K_o,
        80: pygame.K_p,
        81: pygame.K_q,
        82: pygame.K_r,
        83: pygame.K_s,
        84: pygame.K_t,
        85: pygame.K_u,
        86: pygame.K_v,
        87: pygame.K_w,
        88: pygame.K_x,
        89: pygame.K_y,
        90: pygame.K_z,
        98: pygame.K_UP,
        104: pygame.K_DOWN,
        102: pygame.K_RIGHT,
        100: pygame.K_LEFT,
        106: pygame.K_INSERT,
        97: pygame.K_HOME,
        103: pygame.K_END,
        99: pygame.K_PAGEUP,
        105: pygame.K_PAGEDOWN,
        109: pygame.K_RCTRL,
        37: pygame.K_LCTRL,
        113: pygame.K_RALT,
        64: pygame.K_LALT,
    }

    def __contains__(self, item):
        return item in self._tk_to_pygame_dict.keys()

    def tk_to_pg(self, key):
        return self._tk_to_pygame_dict[key]

    def tk_to_pg_name(self, key):
        return pygame.key.name(self._tk_to_pygame_dict[key])


translator = TkPygameInterpreter()
