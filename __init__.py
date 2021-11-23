# Copyright 2016 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime, timedelta
from mycroft import MycroftSkill, intent_handler
from mycroft.messagebus.client import MessageBusClient


class ArztterminSkillOhneRichtlinie(MycroftSkill):
    def __init__(self):
        super(ArztterminSkillOhneRichtlinie, self).__init__()

    def initialize(self):
        pass

    @intent_handler('medikamente.intent')
    def add_unspecified_reminder(self, msg=None):
        self.speak_dialog('medikamente')

    @intent_handler('wiederholung.intent')
    def handleAllInformations(self, message):
        self.speak_dialog('medikamente')

    def stop(self, message=None):
        if self.__cancel_active():
            return True
        else:
            return False

    def shutdown(self):
        if isinstance(self.bus, MessageBusClient):
            self.bus.remove('speak', self.prime)
            self.bus.remove('mycroft.skill.handler.complete', self.notify)
            self.bus.remove('mycroft.skill.handler.start', self.reset)


def create_skill():
    return ArztterminSkillOhneRichtlinie()
