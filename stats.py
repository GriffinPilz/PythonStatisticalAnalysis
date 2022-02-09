from statistics import mode
import math


class DataClean:
    def __init__(self, data):
        self.data = data
        self.length = len(data)

    def calc_mean(self):
        # cannot use sum because it does not accept float values
        temp_var = 0
        for x in self.data:
            temp_var += x
        mean = sum(self.data)/self.length
        return float(mean)

    def calc_median(self, data):
        median = 0
        if data:
            if len(data) >= 2:
                if len(data)-1 % 2 == 0:
                    median = data[int((len(data)-1)/2)]
                else:
                    median = ((data[int(((len(data) - 1) / 2) - .5)]) + (data[int((((len(data)-1) / 2) - .5) + 1)])) / 2
        else:
            if self.length > 2:
                if (self.length-1) % 2 == 0:
                    median = self.data[int((self.length-1)/2)]
                else:
                    median = ((self.data[int(((self.length - 1) / 2) - .5)]) + (self.data[int((((self.length-1) / 2) - .5) + 1)])) / 2
        return median

    def calc_mode(self):
        return mode(self.data)

    def calc_iqr_upper(self):
        iqr_upper = 0
        if self.length >= 4:
            if (self.length-1) % 2 == 0:
                iqr_upper = self.calc_median(self.data[int((self.length-1)/2):-1])
            else:
                iqr_upper = self.calc_median(self.data[int(((self.length-1) / 2) - .5) + 1:-1])
        return iqr_upper

    def calc_iqr_lower(self):
        iqr_lower = 0
        if self.length >= 4:
            if (self.length-1) % 2 == 0:
                iqr_lower = self.calc_median(self.data[0:int((self.length-1)/2)])
            else:
                iqr_lower = self.calc_median(self.data[0:int(((self.length-1) / 2) - .5) + 1])
        return iqr_lower

    def calc_iqr(self):
        iqr_upper = self.calc_iqr_upper()
        iqr_lower = self.calc_iqr_lower()
        return iqr_upper - iqr_lower

    def calc_variance(self):
        sq_sum = 0
        for x in self.data:
            sq_sum += x*x
        return sq_sum/self.length

    def calc_sample_variance(self):
        sq_sum = 0
        for x in self.data:
            sq_sum += x*x
        return sq_sum/(self.length-1)

    def calc_deviation(self):
        if self.calc_variance() >= 0:
            return math.sqrt(self.calc_variance())
        else:
            return math.sqrt(self.calc_variance()*-1) * -1

    def calc_sample_deviation(self):
        if self.calc_variance() >= 0:
            return math.sqrt(self.calc_sample_variance())
        else:
            return math.sqrt(self.calc_sample_variance()*-1) * -1

    def identify_outliers(self):
        outliers = []
        iqr_lower = self.calc_iqr_lower()
        iqr_upper = self.calc_iqr_upper()
        lower_boundary = iqr_lower - 1.5*iqr_lower
        upper_boundary = iqr_upper + 1.5*iqr_upper
        for x in self.data:
            if x < lower_boundary:
                outliers.append(x)
            if x > upper_boundary:
                outliers.append(x)
        return outliers

    def remove_outliers(self):
        outliers = self.identify_outliers()
        if len(outliers):
            for x in outliers:
                self.data.remove(x)
        return self.data

# print("Data mean: ", data_set.calc_mean())
# print("Data median: ", data_set.calc_median(data_list))
# print("Data mode: ", data_set.calc_mode())
# print("Data iqr: ", data_set.calc_iqr())
# print("Data variance: ", data_set.calc_variance())
# print("Data sample variance: ", data_set.calc_sample_variance())
# print("Data deviation: ", data_set.calc_deviation())
# print("Data sample deviation: ", data_set.calc_sample_deviation())
# print("Data sample identify outliers: ", data_set.identify_outliers())
# print("Data sample remove outliers: ", data_set.remove_outliers())
