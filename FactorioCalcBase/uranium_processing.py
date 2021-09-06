class UraniumProcessor:
    def __init__(self, cannot_process_dict: dict, extra_product_rate_dict):
        self.extra_product_rate_dict = extra_product_rate_dict
        self.u235_needed = cannot_process_dict.get('uranium-235')
        self.u238_needed = cannot_process_dict.get('uranium-238')
