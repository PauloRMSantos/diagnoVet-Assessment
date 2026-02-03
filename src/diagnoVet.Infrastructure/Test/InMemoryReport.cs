using diagnoVet.Application.Interfaces;
using diagnoVet.Domain.Entities;

namespace diagnoVet.Infrastructure.Test;

public class InMemoryReport : IReportRepository
{
    private readonly Dictionary<Guid, Report> _db = new();

    public Task SaveAsync(Report report)
    {
        _db[report.Id] = report;
        return Task.CompletedTask;
    }

    public Task<Report?> GetByIdAsync(Guid id)
    {
        _db.TryGetValue(id, out var report);
        return Task.FromResult(report);
    }
}