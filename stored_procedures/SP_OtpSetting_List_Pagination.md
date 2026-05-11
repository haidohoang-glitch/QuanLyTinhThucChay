# Stored Procedure: `OtpSetting_List_Pagination`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-11-26 10:46:13.493000
- **Ngày sửa cuối**: 2014-11-26 10:46:13.493000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@LstId` | `nvarchar` | No |
| `@PBN` | `int(4)` | No |
| `@TypeId` | `int(4)` | No |
| `@PageIndex` | `int(4)` | No |
| `@PageSize` | `int(4)` | No |

## Definition (Source Code)

```sql

-- EXEC [dbo].[OtpSetting_List_Pagination] '',0,0,1,15
CREATE PROCEDURE [dbo].[OtpSetting_List_Pagination]
	@LstId		NVARCHAR(MAX) = '',
	@PBN		INT,
	@TypeId		INT,			
	@PageIndex	INT = 1,
	@PageSize	INT = 15	
AS
BEGIN
  SET NOCOUNT ON
	DECLARE
		@STMT	 NVARCHAR(MAX), -- SQL to execute                     
		@Filter NVARCHAR(MAX) = ' ',
		@MaxRecords	INT 
	   
	IF (@TypeId = 1)
		SET @Filter += ' AND T.DmPhongBanID = ' +  CONVERT(NVARCHAR(9), @PBN)
	ELSE IF (@TypeId = 2)
		SET @Filter += ' AND T.DmBoPhanID = ' +  CONVERT(NVARCHAR(9), @PBN)
	ELSE IF (@TypeId = 3)
		SET @Filter += ' AND T.DmNhomID = ' +  CONVERT(NVARCHAR(9), @PBN)
		
	IF(@LstId <> '')
		SET @Filter += ' AND T.NhanSuSoYeuLyLichID IN (' + @LstId + ')'	      	            

    DECLARE
      @Lbound INT,
      @Ubound INT

    SET @PageIndex = ABS(@PageIndex)
    SET @PageSize  = ABS(@PageSize)
    
    IF @PageIndex < 1 SET @PageIndex = 1
    IF @PageSize < 1 SET @PageSize = 1
    
    SET @Lbound = ((@PageIndex - 1) * @PageSize)
    SET @Ubound = @Lbound + @PageSize + 1
    
    IF @Lbound >= @MaxRecords BEGIN
      SET @Ubound = @MaxRecords + 1
      SET @Lbound = @Ubound - (@PageSize + 1) -- return the last page of records if                                               -- no records would be on the
                                              -- specified page
    END
    
 	SET @STMT =  ' 
 					Select * from
 					(
					SELECT ROW_NUMBER() OVER(ORDER BY T.HoVaTen) AS ItemIndex, T.OxUserID, T.UserName, T.HoVaTen as FullName, T.Email, T.Mobile ,T.NhanSuSoYeuLyLichID,T.RecordStatus  FROM (
						SELECT  													
							A.OxUserID
							,A.Username
							,C.NhanSuSoYeuLyLichID
							,C.HoVaTen
							,E.DmPhongBanID
							,E.TenPhongBan
							,F.DmBoPhanID
							,F.TenBoPhan
							,G.DmNhomID
							,G.TenNhom
							,
							case isnull(replace(A.Email, '' '', ''''),replace(C.Email,'' '', '''')) 
							WHEN '''' THEN replace(C.Email, '' '', '''')
							ELSE isnull(replace(A.Email, '' '', ''''),replace(C.Email, '' '', ''''))
							end AS Email
							,
							case isnull(replace(A.MobileNumber, '' '', ''''),replace(C.Mobile, '' '', '''')) 
							WHEN '''' THEN replace(C.Mobile, '' '', '''')
							ELSE isnull(replace(A.MobileNumber, '' '', ''''),replace(C.Mobile, '' '', '''')) 
							end AS Mobile
							, Isnull(D.RecordStatus,0) as RecordStatus
							FROM ABM_Security.dbo.OxUser A
							LEFT JOIN ABM_Security.dbo.NhanSuQuyenNguoiDung B ON A.OxUserID = B.OxUserREF
							LEFT JOIN ABM_Security.dbo.NhanSuSoYeuLyLich C ON C.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichREF
							LEFT JOIN ABM_Security.dbo.NhanSuQuaTrinhCongTac D ON D.NhanSuSoYeuLyLichREF = C.NhanSuSoYeuLyLichID
							LEFT JOIN ABM_Security.dbo.DmPhongBan  E ON E.DmPhongBanID = D.DmPhongBanREF
							LEFT JOIN ABM_Security.dbo.DmBoPhan F ON F.DmBoPhanID = D.DmBoPhanREF
							LEFT JOIN ABM_Security.dbo.DmNhom G ON G.DmNhomID = D.DmNhomREF
							left join dbo.OtpSetting H ON H.NhanSuSoYeuLyLichID = C.NhanSuSoYeuLyLichID
							WHERE
							C.NgayNghiViec IS NULL
							AND D.[Active] = 1
							) T
						WHERE T.Mobile IS Not NULL AND T.Mobile <> ''''  
					' + @Filter + ')Z where  Z.ItemIndex > ' + CONVERT(varchar(9), @Lbound) + ' AND Z.ItemIndex < ' + CONVERT(varchar(9), @Ubound)
					    


    
    PRINT (@STMT)
                        
    EXEC (@STMT)                 -- return requested records   
END

```
