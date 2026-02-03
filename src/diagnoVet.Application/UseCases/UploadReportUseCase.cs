using diagnoVet.Application.DTOs;
using diagnoVet.Application.Interfaces;
using diagnoVet.Domain.Entities;

namespace diagnoVet.Application.UseCases;

public class UploadReportUseCase
{
    private readonly IFileStorage _fileStorage;
    private readonly IDocumentProcessor _documentProcessor;
    private readonly IReportRepository _reportRepository;

    public UploadReportUseCase(
        IFileStorage fileStorage,
        IDocumentProcessor documentProcessor,
        IReportRepository reportRepository
    )
    {
        _fileStorage = fileStorage;
        _documentProcessor = documentProcessor;
        _reportRepository = reportRepository;
    }

    public async Task<Guid> ExecuteAsync(Stream pdf)
    {
        var reportId = Guid.NewGuid();

        var pdfUri = await _fileStorage.UploadPdfAsync(pdf, $"{reportId}.pdf");

        ExtractedReportData extractedReportData = await _documentProcessor.ProcessDocumentAsync(pdfUri);

        var report = new Report(
            reportId,
            extractedReportData.Patient,
            extractedReportData.Owner,
            extractedReportData.Veterinarian,
            extractedReportData.Diagnosis,
            extractedReportData.Recommendations
        );

        await _reportRepository.SaveAsync(report);
        return reportId;
    }
}