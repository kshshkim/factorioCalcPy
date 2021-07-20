import threading
import time
from FactorioCalcWeb.calculator_interface import CalcInstance


class SessionClass:
    def __init__(self, rand_id: float, default_life_span: int):
        self.id = rand_id
        self.remain_life = default_life_span
        self.calc_instance = CalcInstance()


class SessionManagerClass:
    def __init__(self):
        self.SD = {}
        self.kill_list = []
        self.default_life_span = 3600
        # 정확히 1초는 아니지만 정확히 1초일 필요는 없을듯함
        self.update_cycle = 10

        threading.Thread(target=self.start_session_time_bomb).start()

    def add_session(self, rand_id: float):
        self.SD[rand_id] = SessionClass(rand_id, self.default_life_span)

    def start_session_time_bomb(self):
        # TODO
        while True:
            threading.Timer(self.update_cycle, self.session_time_bomb).start()
            time.sleep(self.update_cycle)

    def session_time_bomb(self):
        # while True:
        for ss in self.SD.values():
            asdf = self.remain_life_counter(ss)
            t = threading.Thread(target=asdf)
            t.start()
        if self.kill_list:
            for victim in self.kill_list:
                del self.SD[victim.id]
            self.kill_list = []
            print('thread all killed')

    def kill_session(self):
        for victim in self.kill_list:
            del self.SD[victim.id]
        self.kill_list = []

    def remain_life_counter(self, ss_obj: SessionClass):
        ss_obj.remain_life -= self.update_cycle
        print('id='+str(ss_obj.id)+'\nremain_life='+str(ss_obj.remain_life))
        if ss_obj.remain_life < 0:
            self.kill_list.append(ss_obj)

    def im_alive(self, rand_id: float):
        not_dead_yet: SessionClass = self.SD[rand_id]
        not_dead_yet.remain_life = self.default_life_span
