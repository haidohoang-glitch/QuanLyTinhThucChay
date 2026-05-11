# Stored Procedure: `Gen_GetParameter_DmHinhThucLaoDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:35:53.553000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.970000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_DmHinhThucLaoDong] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[DmHinhThucLaoDong] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
