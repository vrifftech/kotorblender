# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

from __future__ import annotations

from typing import ClassVar

import bpy

from ...scene.animation import Animation
from ...utils import is_mdl_root


class KB_OT_add_animation(bpy.types.Operator):
    bl_idname: ClassVar[str] = "kb.add_animation"
    bl_label: ClassVar[str] = "Add animation to the list"
    bl_description: ClassVar[str] = "Add a new animation entry to the KotOR model's animation list"

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        if not context.object or not is_mdl_root(context.object):
            cls.poll_message_set(context, "Select a KotOR model object")
            return False
        return True

    def execute(self, context: bpy.types.Context) -> set[str]:
        obj = context.object
        Animation.append_to_object(obj, "newanim", 0, 0.25, obj.name)

        return {"FINISHED"}
