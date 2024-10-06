from . import user_input

class llm_m:
    def __init__(
            self,
            user_text: str = user_input
                 ):
        self.user_test = user_text
    def preprocess_txt(self):
        #Later process the text
        return self.user_test
    def model_inf(self):
        #Later do the model inference here
        return self.user_test
    def get_response(self):
        processed_text = self.preprocess_txt()
        model_response = self.model_inf()
        return model_response


