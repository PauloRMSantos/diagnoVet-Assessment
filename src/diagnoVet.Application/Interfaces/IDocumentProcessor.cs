using diagnoVet.Application.DTOs;

namespace diagnoVet.Application.Interfaces;

public interface IDocumentProcessor
{
    Task<ExtractedReportData> ProcessDocumentAsync(string gcsUri);
}