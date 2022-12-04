import launch_menu as lm
import pytest
import tkinter as tk

class Test_Menu_Variables:
    menu_variables = lm.MenuVariables
    window = tk.Tk()

    def _get_valid_vars(self) -> dict[str, tk.Variable]:
        return {
            "intV": tk.IntVar(value = 4),
            "dblV": tk.DoubleVar(value = 12.3),
            "blnV": tk.BooleanVar(value = False),
            "strV": tk.StringVar(value = "beep beeeeep"),
        }

    def _get_instance(self, input : dict[str, tk.Variable] = {}):
        inner_inst = self.menu_variables()

        for key, val in input.items():
            inner_inst.add(key, val)

        return inner_inst

    def test_add_valid(self):
        valid_vars = self._get_valid_vars()
        inner_instance = self.menu_variables()
        for key, val in valid_vars.items():
            assert inner_instance.add( key, val  ) == key

    def test_add_invalid(self):
        vars = { "intV": tk.IntVar(value = 4), "intV": tk.IntVar(value = 4), "intV": tk.IntVar(value = 4)}
        inner_instance = self._get_instance(vars)
        suffix = ""
        for key in vars.keys():
            assert key == ( "intV" + suffix )
            suffix += "i"

        with pytest.raises( TypeError ) as exc_info:
            inner_instance.add([32, "beeep"])
        
        assert exc_info.type is TypeError

    def test_get(self):
        inner_instance = self._get_instance({"intV": tk.IntVar(value = 4)})
        inner_instance.add( "intV", tk.IntVar(value = 28) )
        # try with invalid key
        with pytest.raises( AttributeError ) as exc_info:
            inner_instance.get(432)
        # valid keys
        assert inner_instance.get("intV") == 4
        assert inner_instance.get("intVi") == 28
        assert exc_info.type is AttributeError
    
    def test_equals(self):
        inner_instance = self._get_instance( {"intV": tk.IntVar(value = 4)} )
        other_instance = self._get_instance( {"intV": tk.IntVar(value = 4)} )

        assert inner_instance == other_instance
    
    def test_update(self):
        inner_instance = self._get_instance( {"intV": tk.IntVar(value = 4)} )
        key = inner_instance.update( "intV", 22)
        with pytest.raises( AttributeError ) as exc_info:
            inner_instance.update(231, "beeep")

        assert inner_instance.get(key) == 22
        assert exc_info.type is AttributeError

    def test_remove(self):
        valids = self._get_valid_vars()
        inner_instance = self._get_instance( valids )
        inner_instance.remove("intV")
        valids.pop("intV")

        with pytest.raises( KeyError ) as exc_info:
            inner_instance.remove("fake_Variable")

        assert inner_instance == self._get_instance( valids )
        assert exc_info.type is KeyError

class Test_Width_Height_Pair:
    def _new_pair(self, width, height):
        return lm.WidthHeightPair(width, height)
    
    def test_properties(self):
        pair = self._new_pair(3, 41)
        assert pair.height == 41
        assert pair.width == 3
        assert pair.pair == (3, 41)

    def test_manipulable(self):
        pair = self._new_pair(3, 10)
        assert pair.width * 5 == 15
        assert pair.height * 5 == 50
