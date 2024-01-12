from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        names = ["Alice", "Bob", "Charlie", "Diana"]
        for name in names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


if __name__ == '__main__':
    DynamicLabelsApp().run()
