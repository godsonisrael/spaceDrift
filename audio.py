from kivy.core.audio import SoundLoader


def init_audio(self):
    self.sound_begin = SoundLoader.load("audio/begin.wav")
    self.sound_gameover_impact = SoundLoader.load("audio/gameover_impact.wav")
    self.sound_gameover_voice = SoundLoader.load("audio/gameover_voice.wav")
    self.sound_music1 = SoundLoader.load("audio/music1.wav")
    self.sound_restart = SoundLoader.load("audio/restart.wav")

    self.sound_music1.volume = 1
    self.sound_begin.volume = .25
    self.sound_gameover_voice.volume = .25
    self.sound_restart.volume = .25
    self.sound_gameover_impact.volume = .6


def game_over_delay(self, dt):
    if self.is_game_over:
        self.sound_gameover_voice.play()
