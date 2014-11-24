class TextChecker:
        source =  ""
        def read(self,str):
                self.source = ""
                for line in str: self.source += line
                return len(self.source)
     
        def check(self,str):
                buf = ""
                for line in str: buf += line
                words = buf.split()
                result = {}
                for word in words: result[word] = self.source.count(word)
                return result

        # search for words in source
        def tc(self,**options):
                keys = ("source","words")
                output = {}
                if keys[0] in options:
                        output["len"] = self.read(options[keys[0]])

                if keys[1] in options:
                        output["count"] = self.check(options[keys[1]])

                return output

