using MediatR;

namespace EmployeeHelper.UseCases.Login;

public record LoginCommand(string Email, string Password) : IRequest<Unit>;
