using diagnoVet.Application.DTOs;
using diagnoVet.Application.Interfaces;

namespace diagnoVet.Infrastructure.Test;

public class TestDocumentProcessor : IDocumentProcessor
{
    public Task<ExtractedReportData> ProcessDocumentAsync(string gcsUri)
    {
        return Task.FromResult(
            new ExtractedReportData(
                "Paciente Teste",
                "Tutor Teste",
                "Veterinário Teste",
                "Diagnóstico Teste",
                "Recomendações Teste"
            )
        );
    }
}