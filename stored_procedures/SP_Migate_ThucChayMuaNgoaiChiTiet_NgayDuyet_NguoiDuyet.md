# Stored Procedure: `Migate_ThucChayMuaNgoaiChiTiet_NgayDuyet_NguoiDuyet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-05-22 17:25:45.240000
- **Ngày sửa cuối**: 2020-06-01 11:37:53.757000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Migate_ThucChayMuaNgoaiChiTiet_NgayDuyet_NguoiDuyet]
*/
CREATE PROCEDURE [dbo].[Migate_ThucChayMuaNgoaiChiTiet_NgayDuyet_NguoiDuyet]
As 	
BEGIN
    DECLARE @NgayThucHien DATETIME, @NgayThucHien_ThucChayMN DATETIME
	DECLARE @SQL NVARCHAR(MAX), @SQL_ThucChayMN NVARCHAR(MAX) = ''

	
	SET @NgayThucHien_ThucChayMN = 
	ISNULL((
			SELECT MAX(dchdct.LastModifiedAt)
			FROM   dbo.ThucChayMuaNgoaiChiTiet dchdct
		),'2010-01-01')

	set @NgayThucHien_ThucChayMN = '1900-01-01' --DATEADD(day,-1,@NgayThucHien_ThucChayMN)
	
	PRINT @NgayThucHien_ThucChayMN

	CREATE TABLE #ThucChayMuaNgoaiChiTiet(
		[ThucChayMuaNgoaiChiTietID] [int] NOT NULL,
		[HopDongREF] [int] NOT NULL,
		[HopDongChiTietREF] [int] NOT NULL,
		[TuNgay] [datetime] NULL,
		[DenNgay] [datetime] NULL,
		[NgayThucChay] [datetime] NULL,
		[SoLuongThucChay] [float] NULL,
		[DmDonViTinhREF] [int] NULL,
		[ChietKhauMuaNgoai] [float] NULL,
		[ThanhTienMuaNgoaiTruocCK] [float] NULL,
		[ThanhTienThucChayBanSauCK] [float] NULL,
		[ThanhTienLaiThucChaySauCK] [float] NULL,
		[CreatedAt] [datetime] NULL,
		[CreatedBy] [nvarchar](50) NULL,
		[LastModifiedAt] [datetime] NULL,
		[LastModifiedBy] [nvarchar](50) NULL,
		[Status_approved] [smallint] NULL,
		[DeletedStatus] [smallint] NULL,
		[NgayDuyet] [Datetime] NULL,
		[NguoiDuyet] [Nvarchar](100),
		[NgayChot] [Datetime] NULL,
		[NguoiChot] [Nvarchar](100),
		[STATUS_MN] INT
	)

	
	INSERT INTO #ThucChayMuaNgoaiChiTiet
	(
	    ThucChayMuaNgoaiChiTietID,
	    HopDongREF,
	    HopDongChiTietREF,
	    TuNgay,
	    DenNgay,
	    NgayThucChay,
	    SoLuongThucChay,
	    DmDonViTinhREF,
	    ChietKhauMuaNgoai,
	    ThanhTienMuaNgoaiTruocCK,
	    ThanhTienThucChayBanSauCK,
	    ThanhTienLaiThucChaySauCK,
	    CreatedAt,
	    CreatedBy,
	    LastModifiedAt,
	    LastModifiedBy,
	    Status_approved,
	    DeletedStatus,
		[NgayDuyet],
		[NguoiDuyet],
		[NgayChot],
		[NguoiChot],
	    [STATUS_MN]
	)
	
	SELECT Id AS ThucChayMuaNgoaiChiTietID,
    HopDongId,
    PhanBoId,
    IIF(NgayBatDau = '0001-01-01','1900-01-01',NgayBatDau) AS NgayBatDau,
    IIF(NgayKetThuc = '0001-01-01','1900-01-01',NgayKetThuc) AS NgayKetThuc,
	CreationTime AS NgayThucChay,
	SoLuongChay,
	D_DonViTinhREF,
    ChietKhauMua,
    ISNULL(SoLuongChay,0)*ISNULL(DonGia,0) AS TienThucChay,
	0 AS ThanhTienThucChayBan,
	0 AS ThanhTienLaiThucChaySauCK,
    CreationTime,
    ISNULL((SELECT TOP (1) t.Username FROM [192.168.23.217].PMS.dbo.V_NhanVien_DangNhap t WHERE t.ID = CreatorUserId ORDER BY t.ID),'') AS Created_By,
    LastModificationTime,
    ISNULL((SELECT TOP (1) t.Username FROM [192.168.23.217].PMS.dbo.V_NhanVien_DangNhap t WHERE t.ID = LastModifierUserId ORDER BY t.ID),'') AS LastModified_By,
	TrangThai, --0 : mới,1: gửi duyệt;2 duyệt thanh toán, 3 -- gửi duyệt thực chạy, --4 duyệt thực chạy
    IsDeleted,
	NgayDuyet,
	ISNULL((SELECT TOP (1) t.tendangnhap FROM [192.168.23.217].PMS.[dbo].[V_NguoiDung] t WHERE t.OxUserID = NguoiDuyet ORDER BY t.OxUserID),'') AS NguoiDuyet,
	NgayChot,
	ISNULL((SELECT TOP (1) t.tendangnhap FROM [192.168.23.217].PMS.[dbo].[V_NguoiDung] t WHERE t.OxUserID = NguoiChot ORDER BY t.OxUserID),'') AS NguoiChot,
	0 AS Statuss FROM [192.168.23.217].PMS.dbo.B_QuanLyThucChay
	WHERE LastModificationTime >= @NgayThucHien_ThucChayMN

	
	-- UPDATE GIA TRI CHO NHUNG BAN GHI DA TON TAI                                      

	UPDATE tc
	SET tc.Status = A.Status_approved
	FROM   #ThucChayMuaNgoaiChiTiet A 
	INNER JOIN  [dbo].[ThucChayMuaNgoaiChiTiet] tc
	ON A.[ThucChayMuaNgoaiChiTietID] = tc.ThucChayMuaNgoaiChiTietID



END



```
