import optparse
class optmini:
    def __init__(self):
        self.optParser = optparse.OptionParser()
        self.optParser.add_option('-e', '--epochs', type='int', dest='epochs')
        self.optParser.add_option('-l', '--learningRate', type='float', dest='learning_rate')
        self.optParser.add_option('-m', '--momentum', type='float', dest='momentum')
        self.optParser.add_option('-i', '--MILOSS', type='float', dest='MI_loss')
        self.optParser.add_option('-D', '--debug', action='store_false', dest='flag')

    def __call__(self, *args, **kwargs):
        (option, args) = self.optParser.parse_args()
        return (option, args)

