using MediatR;

namespace EmployeeHelper.UseCases.Login;

public record LoginCommand(string UserName, string Password) : IRequest<Unit>;
