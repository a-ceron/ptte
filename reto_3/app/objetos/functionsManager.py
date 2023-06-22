"""
Flujo de las diferentes operaciones
"""
import csv
import json

from fastapi import Response

from fastapi.responses import FileResponse


def get_dict(path:str)->dict:
    with open(path, 'r') as f:
        data = csv.reader(f)

        header = next(data)
        skeleton = {
            k:[] for k in header if k != '' 
        }

        header = list(skeleton.keys())
        n = len(header)

        for lines in data:
            for i in range(n):
                if lines[i]:
                    skeleton[header[i]].append(
                        lines[i]
                    )
    return skeleton


def pipeline(path, formato):
    if formato == 'csv':
        return FileResponse(path)
    elif formato == 'json':
        json_data = json.dumps(
            get_dict(
                path
            )
        )
        return Response(content=json_data, media_type="application/json")
    raise ValueError('Formato no valido')
