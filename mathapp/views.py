from django.shortcuts import render
from django.http import JsonResponse
import json

try:
    with open("history.json", "r") as file:
        history = json.load(file)
except FileNotFoundError:
    history = []


def save_history():
    with open("history.json", "w") as file:
        json.dump(history, file)


def index(request):
    endpoints = [
        {
            "url": "/",
            "description": "Lists of all the get endpoint samples",
        },
        {
            "url": "/history",
            "description": "Lists the last 20 operations performed on the server, and the answers.\nThe /history URL works even after a server restart.",
        },
        {"url": "/5/plus/3", "description": "Performs addition: 5 + 3"},
        {"url": "/3/minus/5", "description": "Performs subtraction: 3 - 5"},
        {
            "url": "/3/minus/5/plus/8",
            "description": "Performs multiple operations: 3 - 5 + 8",
        },
        {
            "url": "/3/into/5/plus/8/into/6",
            "description": "Performs complex calculation: 3 * 5 + 8 * 6",
        },
        {"url": "/10/mod/3", "description": "Performs modulo operation: 10 % 3"},
        {"url": "/50/percent/200", "description": "Calculates percentage: 50% of 200"},
    ]

    return render(request, "mathapp/index.html", {"endpoints": endpoints})


def calculate(request, operation):
    parts = operation.split("/")

    try:
        operators = {"plus": "+", "minus": "-",
                     "into": "*", "over": "/", "mod": "%", "percent": "/100*"}
        for i, part in enumerate(parts):
            if part in operators:
                parts[i] = operators[part]

        expr = "".join(parts)
        result = eval(expr)

        history.append({"question": expr, "answer": result})
        save_history()
        if len(history) > 20:
            history.pop(0)

        return JsonResponse({"question": expr, "answer": result})
    except Exception as e:
        return JsonResponse({"error": str(e)})


def get_history(request):
    cleaned_history = []
    for item in history:
        cleaned_history.append(
            {"question": item["question"], "answer": item["answer"]})
    return JsonResponse({"history": cleaned_history}, safe=False)
