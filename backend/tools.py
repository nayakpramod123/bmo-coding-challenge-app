import re
from typing import Dict, Any

class BaseTool:
    def execute(self, params: str) -> Dict[str, Any]:
        raise NotImplementedError

class TextProcessorTool(BaseTool):
    def execute(self, params: str) -> Dict[str, Any]:
        text = params.strip()
        
        if "uppercase" in text.lower() or "upper" in text.lower():
            extracted = self._get_quoted_text(text)
            if not extracted:
                extracted = self._extract_content(text, ["uppercase", "upper", "convert", "make", "to", "this"])
            return {"result": extracted.upper(), "operation": "uppercase"}
            
        if "lowercase" in text.lower() or "lower" in text.lower():
            extracted = self._get_quoted_text(text)
            if not extracted:
                extracted = self._extract_content(text, ["lowercase", "lower", "convert", "make", "to", "this"])
            return {"result": extracted.lower(), "operation": "lowercase"}
            
        if "word count" in text.lower() or "count words" in text.lower() or "count the words" in text.lower():
            extracted = self._get_quoted_text(text)
            if not extracted:
                extracted = self._extract_content(text, ["word", "count", "words", "in", "of", "the"])
            word_count = len(extracted.split())
            return {"result": str(word_count), "operation": "word_count"}
            
        if "reverse" in text.lower():
            extracted = self._get_quoted_text(text)
            if not extracted:
                extracted = self._extract_content(text, ["reverse", "the"])
            return {"result": extracted[::-1], "operation": "reverse"}
        
        return {"result": text.upper(), "operation": "uppercase"}
    
    def _get_quoted_text(self, text):
        if '"' not in text and "'" not in text:
            return None
        match = re.search(r'["\']([^"\']+)["\']', text)
        return match.group(1) if match else None
    
    def _extract_content(self, text, remove_words):
        text = text.replace('"', '').replace("'", '')
        words = text.split()
        result = []
        
        for i, word in enumerate(words):
            clean_word = word.lower().strip('.,!?')
            if clean_word in remove_words:
                continue
            if i > 0 and words[i-1].lower() in ["convert", "make", "change"] and clean_word == "to":
                continue
            result.append(word)
        
        content = ' '.join(result).strip()
        if content:
            return content
            
        for keyword in remove_words:
            if keyword in text.lower():
                parts = text.lower().split(keyword, 1)
                if len(parts) > 1:
                    return parts[1].strip()
        
        return text

class CalculatorTool(BaseTool):
    def execute(self, params: str) -> Dict[str, Any]:
        text = params.strip()
        expression = self._extract_expression(text)
        
        try:
            expression = expression.replace("x", "*").replace("X", "*").replace("÷", "/")
            
            if not re.match(r'^[\d\s\+\-\*\/\(\)\.]+$', expression):
                return {"result": "Invalid expression", "expression": expression, "error": True}
            
            result = eval(expression)
            return {"result": str(result), "expression": expression, "error": False}
        except Exception as e:
            return {"result": f"Error: {str(e)}", "expression": expression, "error": True}
    
    def _extract_expression(self, text):
        keywords = ["calculate", "compute", "what is", "what's", "solve", "find", "equals", "equal to"]
        expression = text.lower()
        
        for keyword in keywords:
            expression = expression.replace(keyword, "")
        
        expression = expression.strip()
        if "?" in expression:
            expression = expression.split("?")[0].strip()
        
        return expression

class WeatherMockTool(BaseTool):
    def execute(self, params: str) -> Dict[str, Any]:
        text = params.strip()
        city = self._get_city(text)
        
        weather = {
            "new york": {"temp": 22, "condition": "Partly Cloudy"},
            "london": {"temp": 15, "condition": "Rainy"},
            "tokyo": {"temp": 18, "condition": "Sunny"},
            "paris": {"temp": 16, "condition": "Cloudy"},
            "toronto": {"temp": 10, "condition": "Snowy"},
            "mumbai": {"temp": 30, "condition": "Humid"},
        }
        
        city_key = city.lower()
        if city_key in weather:
            data = weather[city_key]
            result = f"{city.title()}: {data['temp']}°C, {data['condition']}"
        else:
            result = f"{city.title()}: 20°C, Clear (Mock Data)"
        
        return {"result": result, "city": city.title()}
    
    def _get_city(self, text):
        text = text.replace('"', '').replace("'", '')
        skip = ["weather", "temperature", "forecast", "climate", "in", "at", "for", "of", "the"]
        
        words = text.split()
        city_parts = []
        
        for word in words:
            clean = word.lower().strip('.,!?')
            if clean not in skip:
                city_parts.append(word)
        
        city = ' '.join(city_parts).strip()
        return city if city else text