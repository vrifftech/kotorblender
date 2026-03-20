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

import bpy

from ....utils import is_mdl_root


class KB_OT_delete_anim_event(bpy.types.Operator):
    bl_idname = "kb.delete_anim_event"
    bl_label = "Delete event from the animation"
    bl_description = "Remove the selected event from the current animation"
    bl_options = {"UNDO"}

    @classmethod
    def poll(cls, context):
        obj = context.object
        if not obj or not is_mdl_root(obj):
            cls.poll_message_set(context, "Select a KotOR model object")
            return False
        anim_list = obj.kb.anim_list
        anim_list_idx = obj.kb.anim_list_idx
        if anim_list_idx < 0 or anim_list_idx >= len(anim_list):
            cls.poll_message_set(context, "Select an animation in the list")
            return False
        anim = anim_list[anim_list_idx]
        if anim.event_list_idx < 0 or anim.event_list_idx >= len(anim.event_list):
            cls.poll_message_set(context, "Select an event in the animation")
            return False
        return True

    def execute(self, context):
        mdl_root = context.object
        anim = mdl_root.kb.anim_list[mdl_root.kb.anim_list_idx]

        if anim.event_list_idx == len(anim.event_list) - 1 and anim.event_list_idx > 0:
            anim.event_list_idx -= 1

        anim.event_list.remove(anim.event_list_idx)

        return {"FINISHED"}
