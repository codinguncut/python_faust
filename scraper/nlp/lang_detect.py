import cld2


class NoLanguageDetected(Exception):
    pass


def detect(string):
    isReliable, numBytes, details = cld2.detect(string)
    if not isReliable or not details:
        raise NoLanguageDetected(string)

    l_name, l_code, l_percent, l_normed = details[0]
    return {
        'code': l_code,
        'score': l_percent / 100.0
    }
