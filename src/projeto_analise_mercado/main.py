#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from projeto_analise_mercado.crew import ProjetoAnaliseMercado

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Tecnologia da Informação (TI)',
        'current_year': str(datetime.now().year)
    }
    
    try:
        ProjetoAnaliseMercado().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

