import hal

class VaccumPump:
    def __init__(self, halcomp, builder, useropts):
        self.halcomp = halcomp
        self.halcomp.newpin("pump", hal.HAL_BIT, hal.HAL_OUT)

    def on_vacuum_pump_toggled(self, button, data=None):
        self.halcomp["pump"] = button.get_active()

def get_handlers(halcomp, builder, useropts):
    return [VaccumPump(halcomp, builder, useropts)]
